from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Dulces.html', {})

def registro(request):
    return render(request, 'registro.html', {})

def login(request):
    return render(request, 'login.html', {})

def productos(request):
    return render(request, 'productos.html', {})