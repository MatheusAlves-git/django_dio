from django.shortcuts import render, HttpResponse
# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {str(nome).capitalize()}, você tem {idade} anos!</h1><button>Click</button>')