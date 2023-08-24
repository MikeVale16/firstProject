from django.contrib import admin
from django.urls import path


from .views import list_koders,get_koder

urlpatterns = [
path("listkoders/",list_koders),
path("getkoder/",get_koder),
]