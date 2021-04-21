from django.utils import timezone
from rest_framework import serializers
from .models import (
    PricingInfo,
    HistoryPricing,
    Vehicule,
)

class VehiculeSerializer(serializers.Serializer):

    class Meta:
        fields = "__all__"
        model = Vehicule


class CheckingPriceSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    marque = serializers.ChoiceField([v.marque for v in Vehicule.objects.all()])
    modele = serializers.ChoiceField([v.modele for v in Vehicule.objects.all()])
    nb_km = serializers.FloatField()
    nb_rayure = serializers.IntegerField()
