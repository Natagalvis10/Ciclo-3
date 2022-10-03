from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django import forms
from .models import *

#FORMS DE VETERINARIO
class VeterinarioForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Nombre de usuario"
        }
    ))
    password = forms.CharField(max_length=120, label='contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    rol=forms.ModelChoiceField(label='Rol', queryset=Group.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombres= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    apellidos= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    tipo_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    num_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    celular= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    num_profesional= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    class Meta:
        model= Veterinario
        fields= ['username','password','rol','email','nombres','apellidos','tipo_documento','num_documento','celular','num_profesional']

#FORMS DE CLIENTE
class ClienteForm(forms.ModelForm):
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
    rol=forms.ModelChoiceField(label='Rol', queryset=Group.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombres= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    apellidos= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    tipo_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    num_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    celular= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    class Meta:
        model= cliente
        fields= ['username','password','rol','email','nombres','apellidos','tipo_documento','num_documento','celular']

#FORMS DE GRUPOS
class GroupsForm(forms.ModelForm):
    name = forms.CharField(max_length=80, label='Rol', widget=forms.TextInput(
        attrs={'class': 'form-control'
        }
    ))
    permisos=forms.ModelMultipleChoiceField(label='Permisos',
        queryset=Permission.objects.filter(content_type__app_label='veterinariaapp'), 
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select'
            }
        )
    )
    class Meta:
        model= Group
        fields= '__all__'

#FORMS PARA EL LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        }
    ))
    password = forms.CharField(max_length=80, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

#FORMS DE MASCOTA
class MascotaFrom(forms.ModelForm):
    cliente=forms.ModelChoiceField(label='cliente', queryset=cliente.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    nobre= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    raza= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    sexo= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    especie= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    color= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    edad= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    peso= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    class Meta:
        model= Mascota
        fields= ['cliente','nobre','raza','sexo','especie','color','edad','peso']

#FORMS DE  REGISTRO
class RegistroFrom(forms.ModelForm):
    mascota=forms.ModelChoiceField(label='mascota', queryset=Mascota.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    veterinario=forms.ModelChoiceField(label='veterinario', queryset=Veterinario.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    num_histial= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    fecha= forms.DateField(widget=(forms.DateInput(
        attrs={
            'class': "form-control"
        }
    )))
    motivo= forms.CharField(max_length=120, widget=(forms.Textarea(
        attrs={
            'class': "form-control",
            
        }
    )))
    anamnesicos= forms.CharField(max_length=120, widget=(forms.Textarea(
        attrs={
            'class': "form-control",
            
        }
    )))
    diagnostico= forms.CharField(max_length=120, widget=(forms.Textarea(
        attrs={
            'class': "form-control",
            
        }
    )))
    tratamiento= forms.CharField(max_length=120, widget=(forms.Textarea(
        attrs={
            'class': "form-control",
        
        }
    )))
    class Meta:
        model= Registro
        fields= ['mascota','veterinario','num_histial','fecha','motivo','anamnesicos','diagnostico','tratamiento']
