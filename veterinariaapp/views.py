from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import VeterinarioForm, GroupsForm, LoginForm, ClienteForm
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#VISTA DEL HOME PAGE
def home(request):
    return render(request, 'home/index.html')

#VISTA DEL LOGIN PAGE

def login_user(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse('home'))
            else:
                form = LoginForm()
                messages.add_message(request, messages.ERROR, 'Las credenciales no son correctas')
                return render(request, 'acceso/login.html', {'form': form})
        else:    
            return render(request, 'acceso/login.html')
    else:
        form = LoginForm()
        return render(request, 'acceso/login.html', {'form': form})

#VISTA DEL LOGOUT PAGE
@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('home'))

#CRUD DEL MODELO DE ROLES
#TABLA DEL MODELO DE ROLES
@login_required(login_url='/login/')
def listar_rol(request):
    roles= Group.objects.all()
    return render(request, 'roles/index.html',{'roles':roles})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE ROLES
@login_required(login_url='/login/')
def crear_rol(request):
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            rol=form.save()
            mensaje=f'El rol fue agreado correctamente'
            contenido=form.cleaned_data['contenido']
            permisos = Permission.objects.filter(content_type=contenido)
            contexto={
                'permisos':permisos,
                'rol':rol,
                }
            return render(request, 'roles/permisos.html', contexto)
        else:
            mensaje = 'Error al crear el Rol'
            return render(request, 'layout/mensaje.html',{'mensaje':mensaje})
    else:
        form = GroupsForm()
        return render(request, 'roles/rolform.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ELIMINAR DEL MODELO DE ROLES
@login_required(login_url='/login/')
def eliminar_rol(request, id):
    rol=Group.objects.get(id=id)
    if request.method == 'POST':
        rol.delete()
        mensaje= f'El rol {rol} fue eliminado correctamente'
        return redirect('lista-rol')
    return render(request, 'roles/eliminar_rol.html',{'rol':rol})

#LOGICA BASA EN FUNCIONES DE AGREGAR PERMISOS A LOS GRUPOS-ROLES
def agregar_permisos(request):
    if request.method == 'POST':
        permisos = request.POST.getlist('permisos')
        rol = Group.objects.get(id = request.POST.get('rol'))
        rol.permissions.set(permisos)
        return HttpResponse("Hecho")

#CRUD DEL MODELO DEL VETERINARIO
#TABLA DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
def lista_veterinario(request):
    veterinarios= Veterinario.objects.all().order_by('id')
    return render(request, 'veterinario/lista_veterinario.html',{'veterinarios':veterinarios})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
def crear_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email=form.cleaned_data['email']
            nombres=form.cleaned_data['nombres']
            apellidos=form.cleaned_data['apellidos']
            tipo_documento=form.cleaned_data['tipo_documento']
            num_documento= form.cleaned_data['num_documento']
            celular= form.cleaned_data['celular']
            rol=form.cleaned_data['rol']
            veterinario=form.save(commit=False)
            persona = Persona.objects.create_user(
                username=username, 
                password=password,
                email=email,
                first_name=nombres,
                last_name=apellidos,
                tipo_documento=tipo_documento,
                num_documento=num_documento,
                celular=celular
                )
            persona.groups.add(rol)
            veterinario.persona = persona
            veterinario.save()
            mensaje=f'El veterinario {veterinario} fue agreado correctamente'
            return render(request, 'layout/mensaje.html',{'mensaje':mensaje})
            pass
        else:
            mensaje=f'El veterinario {veterinario} fue agreado'
            return render(request, 'layout/mensaje.html',{'mensaje':mensaje})
    else:
        form= VeterinarioForm()
        return render (request,'veterinario/crear_veterinario.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ACTUALIZAR DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
def actualizar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            veterinario= form.save()
            mensaje= f'El veterinario {veterinario} fue actualizado correctamente'
        else:
            mensaje= f'El veterinario {veterinario} no fue actualizado'
        return render (request,'layout/mensaje.html',{'mensaje':mensaje})
    else:
        form = VeterinarioForm(instance=veterinario)
        return render(request, 'veterinario/crear_veterinario.html',{'form':form})  

#LOGICA BASA EN FUNCIONES DE ELIMINAR DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
def eliminar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    if request.method == 'POST':
        veterinario.delete()
        #mensaje= f'El veterinario {veterinario} fue eliminado correctamente'
        return redirect('lista-veterinarios')
    return render(request, 'veterinario/eliminar_veterinario.html',{'veterinario':veterinario})

#CRUD DEL MODELO DEL CLIENTE
#TABLA DEL MODELO DE CLIENTE
@login_required(login_url='/login/')
def lista_cliente(request):
    clientes= cliente.objects.all()
    return render(request, 'cliente/lista_cliente.html',{'clientes':clientes})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE VETERINARIO
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente=form.save()
            
    else:
        form = ClienteForm()
        return render(request, 'cliente/crear_cliente.html',{'form':form})

