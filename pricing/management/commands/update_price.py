from django.core.management.base import BaseCommand, CommandError
import requests

from pricing.models import PricingInfo, HistoryPricing

def format_price_info(price_info):
    if price_info.get("prix_km"):
        price_info["price_km_supp"] = price_info.get("prix_km", 0)
        del price_info["prix_km"]
    if price_info.get("prix_rayure"):
        price_info["price_rayure"] = price_info.get("prix_rayure", 0)
        del price_info["prix_rayure"]
    return price_info

class Command(BaseCommand):
    help = "Permet de mettre à jour la liste des prix en passant l'addresse du serveur à requêter"

    def add_arguments(self, parser):
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        req = requests.get(f"http://{options.get('address')}/PricingInfo")
        for price_info in req.json():
            price_info = format_price_info(price_info)
            try:
                p = PricingInfo.objects.get(marque=price_info.get("marque"), modele=price_info.get("modele"))
                if p.price_km_supp != price_info.get("price_km_supp") or p.price_rayure != price_info.get("price_rayure"):
                    copied_item = p.__dict__.copy()
                    del copied_item["id"]
                    del copied_item["_state"]
                    history_p = HistoryPricing(**copied_item)
                    history_p.save()
                    p.delete()
                    PricingInfo(**price_info).save()
                    self.stdout.write(self.style.SUCCESS("Récupération des données réussies ! (Modification de données)"))
            except PricingInfo.DoesNotExist:
                p = PricingInfo(**price_info)
                p.save()
                self.stdout.write(self.style.SUCCESS("Récupération des données réussies ! (Nouvelle données)"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(e))
