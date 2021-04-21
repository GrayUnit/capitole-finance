from django.contrib import admin
from .models import (
    Category,
    Vehicule,
    PricingInfo,
    HistoryPricing
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Vehicule)
admin.site.register(PricingInfo)
admin.site.register(HistoryPricing)