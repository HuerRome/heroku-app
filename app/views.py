from django.shortcuts import render

# Create your views here.
#/demo/views.py
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")
