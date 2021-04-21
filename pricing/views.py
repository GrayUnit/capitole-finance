from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
)
from django.http import HttpResponse, Http404
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vehicule, PricingInfo, HistoryPricing
from .serializers import CheckingPriceSerializer

# Create your views here.
class IndexView(generic.ListView):
    template_name = "pricing/index.html"
    context_object_name = "list_vehicules"

    def get_queryset(self):
        return Vehicule.objects.all()

@login_required
def calculator(request, id_vehicule):
    vehicule = get_object_or_404(Vehicule, pk=id_vehicule)
    return render(request, "pricing/calculator.html", {"vehicule": vehicule})

@login_required
def calcul(request, id_vehicule):
    vehicule: Vehicule = get_object_or_404(Vehicule, pk=id_vehicule)
    pricing_info: PricingInfo = get_object_or_404(PricingInfo, modele=vehicule.modele, marque=vehicule.marque)
    total_price = vehicule.initial_price
    price_km_supp = (float(request.POST["km_actuel"]) - vehicule.km_initial) * pricing_info.price_km_supp
    price_rayure_supp = float(request.POST["nb_rayure"]) * pricing_info.price_km_supp
    total_price += price_km_supp + price_rayure_supp
    request.session["total"] = total_price
    return redirect(reverse('pricing:result'))

@login_required
def result(request):
    return render(request, "pricing/result.html", {"total": request.session["total"]})


class CheckPricing(APIView):
    serializer_class = CheckingPriceSerializer

    def post(self, request, format=None):
        data = request.data
        vehicule: Vehicule = get_object_or_404(Vehicule, modele=data.get("modele"), marque=data.get("marque"))
        total_price = vehicule.initial_price
        try:
            pricing = PricingInfo.objects.get(modele=data.get("modele"), marque=data.get("marque"), date_modification__lte=data.get("date"))
        except PricingInfo.DoesNotExist:
            pricing = HistoryPricing.objects.filter(
                modele=data.get("modele"),
                marque=data.get("marque"),
                date_modification__lte=data.get("date")
            ).latest("date_modification")
        price_km_supp = (float(data.get("nb_km")) - vehicule.km_initial) * pricing.price_km_supp
        price_rayure_supp = float(data.get("nb_rayure")) * pricing.price_km_supp
        total_price += price_km_supp + price_rayure_supp
        return Response({"Total": total_price})
