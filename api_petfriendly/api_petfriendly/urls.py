"""
URL configuration for api_petfriendly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pet_friendly import views

urlpatterns = [
    path('animales/', views.obtener_lista_animales, name='lista_animales'),
    path('animales/create/', views.agregar_animal, name='agregar_animal'),
    path('animales/contactos/', views.agregar_contacto, name='agregar_contacto'),
    path('animales/contactos_registro/', views.agregar_contacto, name='agregar_registro'),
]