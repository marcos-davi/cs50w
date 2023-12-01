from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("marcos", views.marcos, name="marcos"),
    path("davi", views.davi, name="davi")

]