from django import forms
from .models import Employe
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': "Nom d'utilisateur"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'Mot de passe'
    }))

class EmployeForm(forms.ModelForm) :
    class Meta :
        model = Employe
        fields = ['nom', 'email', 'poste', 'salaire']
        widgets = {
            'nom' : forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Nom'
            }),
            'email': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'E-mail'
            }),
            'poste': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Poste'
            }),
            'salaire': forms.TextInput(attrs = {
                'class' : 'input w-full',
                'placeholder' : 'Salaire'
            })
        }