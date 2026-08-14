from django.urls import path
from . import  views
urlpatterns = [
    path('', views.liste_employes, name='liste_employes'),
    path('ajouter', views.ajouter_employes, name='ajouter_employe'),
path('modifier/<int:id>/', views.modifier_employes, name='modifier_employe'),
]