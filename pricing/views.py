from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Vehicule

# Create your views here.
def index(request):
    list_vehicules = Vehicule.objects.all()
    context = {"list_vehicules": list_vehicules}
    return render(request, 'pricing/index.html', context)

def calculator(request, id_vehicule):
    vehicule = get_object_or_404(Vehicule, pk=id_vehicule)
    return render(request, "pricing/calculator.html", {"vehicule": vehicule})
