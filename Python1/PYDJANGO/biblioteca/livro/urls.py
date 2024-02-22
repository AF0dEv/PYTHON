from django.urls import path
from . import views # from diretorio atual import views

urlpatterns = [
    path("registar/", views.registar)
]

