from django.http import HttpResponse
from django.shortcuts import render
from .forms import VeterinarioFrom
from .models import *

#crear vista home
def home(request):
    return render(request, 'home/index.html')

#tabla de los datos del o de los 
def lista_veterinario(request):
    veterinarios= Veterinario.objects.all()
    return render(request, 'veterinario/lista_veterinario.html',{'veterinarios':veterinarios})

# Crear las vistas aqui 
def crear_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioFrom(request.POST)
        if form.is_valid():
            veterinario=form.save()
            mensaje=f'El veterinario {veterinario} fue agreado correctamente'
            return render(request, 'veterinario/mensaje.html',{'mensaje':mensaje})
            pass
        else:
            mensaje=f'El veterinario {veterinario} fue agreado'
            return render(request, 'veterinario/mensaje.html',{'mensaje':mensaje})
    else:
        form= VeterinarioFrom()
        return render (request,'veterinario/crear_veterinario.html',{'form':form})
    
#eliminar -CRUD- veterinario
def borrar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    veterinario.delete()
    mensaje= f'El veterinario {veterinario} fue eliminado correctamente'
    return render(request, 'veterinario/mensaje.html',{'mensaje':mensaje})