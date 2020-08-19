from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def evento(request, titulo):
    return HttpResponse(Evento.objects.get(titulo=titulo))