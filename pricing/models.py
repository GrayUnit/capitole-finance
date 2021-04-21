from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, blank = False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "{id}-{title}".format(id=self.id, title=self.name)


class Vehicule(models.Model):
    marque = models.CharField(max_length=255, default="marque")
    modele = models.CharField(max_length=255, default="modele")
    description = models.CharField(max_length=255)
    km = models.PositiveIntegerField()
    moteur = models.FloatField()
    carburant = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank = True, on_delete=models.SET_NULL)


class PricingInfo(models.Model):
    marque = models.CharField(max_length=255, default="marque")
    modele = models.CharField(max_length=255, default="modele")
    price_km_supp = models.FloatField()
    price_rayure = models.FloatField()
