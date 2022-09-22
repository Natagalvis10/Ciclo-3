from django.contrib.auth.models import Group
from django import forms
from .models import *

#se crea el formulario para veterinario 

class VeterinarioForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Nombre de usuario"
        }
    ))
    password = forms.CharField(max_length=120, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.EmailField()
    nombres= forms.CharField(max_length=120)
    apellidos= forms.CharField(max_length=120)
    tipo_documento= forms.CharField(max_length=20)
    num_documento= forms.CharField(max_length=20)
    celular= forms.CharField(max_length=10)
    class Meta:
        model= Veterinario
        fields= ['num_profesional']
        
   
        
#FORMULARIO PARA CREAR LOS GRUPOS
class GroupsForm(forms.ModelForm):
    name = forms.CharField(max_length=80, label='Rol', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    class Meta:
        model= Group
        fields='__all__'
    