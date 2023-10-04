from django.urls import path

from .import views

urlpatterns = [
    path("", views.index, name="index"),
     # Aqui entro los paths de cada página de mi proyecto
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet")


]