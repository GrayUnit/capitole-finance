from django.contrib import admin
from django.urls import path
from . import views

app_name = "pricing"
urlpatterns = [
    path('', views.index, name="index"),
    path('calculator/<int:id_vehicule>', views.calculator, name="calculator"),
]
