from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Una view o vista es la página web dinamicamente generada
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("<h1>Hello, Brian</h1>")

# Función para crear views
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
