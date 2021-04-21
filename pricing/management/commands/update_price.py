from django.core.management.base import BaseCommand, CommandError
import requests

from pricing.models import PricingInfo

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
                p = PricingInfo(**price_info)
                p.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR(e))
            else:
                self.stdout.write(self.style.SUCCESS("Récupération des données réussies !"))