from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenue sur la page index")

def calculator(request, id_vehicule):
    return HttpResponse(f"Bienvenue sur la page calculator {id_vehicule}")
