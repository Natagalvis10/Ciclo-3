from django.contrib.auth.models import Group
from django import forms
from .models import *

#se crea el formulario para veterinario 

class VeterinarioFrom(forms.ModelForm):
    usuario = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = forms.CharField(max_length=120, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
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
    