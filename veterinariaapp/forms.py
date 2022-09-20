from tkinter import Widget
from django import forms
from .models import *

#se crea el formulario para veterinario 
class VeterinarioFrom(forms.ModelForm):
    #Parte del formulario del modelo de persona
    tipo_documento = forms.CharField(max_length=20)
    num_documento = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100)
    celular= forms.CharField(max_length=10)
        
    #parte del formulario del modelo de usuario
    username= forms.CharField(max_length=20)
    password= forms.CharField(max_length=20)
    email= forms.EmailField()
    nombres= forms.CharField(max_length=120)
    apellidos= forms.CharField(max_length=120)
    
    class Meta:
        model= Veterinario
        #Lista de los fiels
        fields= ['num_profesional']
        ''' label={'num_profesional':'num_profesional'}
        Widgets={'num_profesional':forms.CharField(max_length=20)}'''
