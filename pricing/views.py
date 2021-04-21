from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
)
from django.http import HttpResponse, Http404

from .models import Vehicule, PricingInfo

# Create your views here.
def index(request):
    list_vehicules = Vehicule.objects.all()
    context = {"list_vehicules": list_vehicules}
    return render(request, 'pricing/index.html', context)

def calculator(request, id_vehicule):
    vehicule = get_object_or_404(Vehicule, pk=id_vehicule)
    return render(request, "pricing/calculator.html", {"vehicule": vehicule})

def calcul(request, id_vehicule):
    vehicule: Vehicule = get_object_or_404(Vehicule, pk=id_vehicule)
    pricing_info: PricingInfo = get_object_or_404(PricingInfo, modele=vehicule.modele, marque=vehicule.marque)
    total_price = vehicule.initial_price
    price_km_supp = (float(request.POST["km_actuel"]) - vehicule.km_initial) * pricing_info.price_km_supp
    price_rayure_supp = float(request.POST["nb_rayure"]) * pricing_info.price_km_supp
    total_price += price_km_supp + price_rayure_supp
    request.session["total"] = total_price
    return redirect(reverse('pricing:result'))

def result(request):
    return render(request, "pricing/result.html", {"total": request.session["total"]})