from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "accounts/login.html"


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('pricing:index'))
    else:
        return HttpResponse("Identifiant ou mot de passe incorrect", status=401)

def log_out(request):
    logout(request)
    return redirect(reverse('accounts:login'))