from django.contrib import admin
from .models import (
    Category,
    Vehicule,
    PricingInfo,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Vehicule)
admin.site.register(PricingInfo)
