from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_koder(request):
    return HttpResponse("Esta es un koder")

def list_koders(request):
    return HttpResponse("Este es una lista de koders")