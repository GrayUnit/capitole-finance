from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, blank = False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "{id}-{title}".format(id=self.id, title=self.name)


class Car(models.Model):
    description = models.CharField(max_length=255)
    km = models.PositiveIntegerField()
    moteur = models.FloatField()
    transmission = models.CharField(max_length=10)
    carburant = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(Category, null=True, blank = True, on_delete=models.SET_NULL)
    searched_counter = models.IntegerField(default=0)
