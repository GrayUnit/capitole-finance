from django.contrib import admin
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.IndexView.as_view(), name="login"),
    path('loginrequest/', views.log_in, name="loginrequest"),
    path('logout/', views.log_out, name="logout"),
]
