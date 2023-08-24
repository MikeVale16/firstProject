from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bienvenida(request):
    return HttpResponse("Bienvenido")

def despedida(request):
    return HttpResponse("Adios perro y no vuelvas")

def saludo(request):
    return HttpResponse("Hola Koders")

def hi_name(request,name):
    return HttpResponse(f"Hola {name}")

def shallnotpass(request,type):
    if type=="mentor":
        return HttpResponse("Hello mentor here are your classes")
    if type=="koder":
        return HttpResponse("Hello koder welcome to kodemia")
    else:
        return HttpResponse("You are not welcome here!")