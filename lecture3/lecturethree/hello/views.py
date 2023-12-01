from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def marcos(request):
    return HttpResponse("Hello, Marcos!")

def davi(request):
    return HttpResponse("Hello, Davi!")

def greet(request, name):
    return render(request,"hello/greet.html", {
        "name":name.capitalize()
        })
