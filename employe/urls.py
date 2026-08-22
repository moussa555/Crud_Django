from django.urls import path
from django.contrib.auth import views as auth_views
from . import  views
from .forms import CustomAuthenticationForm
urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='employe/login.html', authentication_form=CustomAuthenticationForm
    ), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.liste_employes, name='liste_employes'),
    path('ajouter', views.ajouter_employes, name='ajouter_employe'),
    path('modifier/<int:id>/', views.modifier_employes, name='modifier_employe'),
    path('supprimer/<int:id>/', views.supprimer_employe, name='supprimer_employe'),

]