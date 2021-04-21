from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('calculator/<int:id_vehicule>', views.calculator, name="calculator"),
]
