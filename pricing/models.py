from django.db import models
from django.utils import timezone

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
    km_initial = models.PositiveIntegerField()
    moteur = models.FloatField(default=0)
    carburant = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank = True, on_delete=models.SET_NULL)
    initial_price = models.FloatField(default=0)


class PricingInfo(models.Model):
    marque = models.CharField(max_length=255, default="marque")
    modele = models.CharField(max_length=255, default="modele")
    price_km_supp = models.FloatField()
    price_rayure = models.FloatField()
    date_modification = models.DateTimeField(default=timezone.now())


class HistoryPricing(models.Model):
    marque = models.CharField(max_length=255, default="marque")
    modele = models.CharField(max_length=255, default="modele")
    price_km_supp = models.FloatField()
    price_rayure = models.FloatField()
    date_modification = models.DateTimeField()
