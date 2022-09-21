from django.http import HttpResponse
from django.shortcuts import render
from .forms import VeterinarioFrom
from .models import *
from django.contrib.auth.models import User

#crear vista home
def home(request):
    return render(request, 'home/index.html')

#tabla de los datos del o de los 
def lista_veterinario(request):
    veterinarios= Veterinario.objects.all().order_by('id')
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
    


#Actualizar CRUD veterinario
def actualizar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    if request.method == 'POST':
        form = VeterinarioFrom(request.POST, instance=veterinario)
        if form.is_valid():
            veterinario= form.save()
            mensaje= f'El veterinario {veterinario} fue actualizado correctamente'
        else:
            mensaje= f'El veterinario {veterinario} no fue actualizado'
        return render (request,'veterinario/mensaje.html',{'mensaje':mensaje})
    else:
        form = VeterinarioFrom(instance=veterinario)
        return render(request, 'veterinario/crear_veterinario.html',{'form':form})

#eliminar -CRUD- veterinario
def eliminar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    veterinario.delete()
    mensaje= f'El veterinario {veterinario} fue eliminado correctamente'
    return render(request, 'veterinario/eliminar_veterinario.html',{'veterinario':veterinario})