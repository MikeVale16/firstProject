
from django.contrib import admin
from django.urls import path

from .views import despedida,bienvenida,saludo,hi_name,shallnotpass

urlpatterns = [
    path("",bienvenida),
    path("despedida/",despedida),
    path("saludo/",saludo),
    path("hiname/<str:name>",hi_name),
    path("kodemia/<str:type>",shallnotpass)


]
