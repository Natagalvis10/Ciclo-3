from django import forms
from .models import *

#se crea el formulario para veterinario 
class VeterinarioFrom(forms.ModelForm):
    class Meta:
        model= Veterinario
        fields= '__all__'
