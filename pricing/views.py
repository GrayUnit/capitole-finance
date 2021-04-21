from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Vehicule

# Create your views here.
def index(request):
    return HttpResponse("Bienvenue sur la page index")

def calculator(request, id_vehicule):
    try:
        vehicule = Vehicule.objects.get(pk=id_vehicule)
    except Vehicule.DoesNotExist:
        raise Http404("Vehicule introuvable")
    else:
        return HttpResponse(f"{vehicule.__dict__}")
