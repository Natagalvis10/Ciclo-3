from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView

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
            grupo= form.save()
            permisos= form.cleaned_data["permisos"]
            grupo.permissions.set(permisos)
            messages.success(request, "Rol almacenado correctamente")
        else:
            messages.error(request, "Error al crear rol")
        return redirect(reverse('lista-rol'))
    else:
        form = GroupsForm()
        return render(request, 'roles/rolform.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ACTUALIZAR DEL MODELO DE ROLES
def actualizar_rol(request, id):
    pass

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
@permission_required('veterinariaapp.view_veterinario', raise_exception=True)
def lista_veterinario(request):
    veterinarios= Veterinario.objects.all().order_by('id')
    return render(request, 'veterinario/lista_veterinario.html',{'veterinarios':veterinarios})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
@permission_required('veterinariaapp.add_veterinario', raise_exception=True)
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
            messages.success(request, "Los datos del veterinario {veterinario} fueron almacenados correctamente")
        else:
            messages.error(request, "Verifique los datos e intente nuevamente") 
        return redirect(reverse('lista-veterinarios'))
    else:
        form= VeterinarioForm()
        return render (request,'veterinario/crear_veterinario.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ACTUALIZAR DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
@permission_required('veterinariaapp.change_veterinario', raise_exception=True)
def actualizar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    if request.method == 'GET':
        form = VeterinarioForm(instance=veterinario)
    else:
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
        return redirect(reverse('lista-veterinarios'))
    return render(request, 'veterinario/crear_veterinario.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ELIMINAR DEL MODELO DE VETERINARIO
@login_required(login_url='/login/')
@permission_required('veterinariaapp.delete_veterinario', raise_exception=True)
def eliminar_veterinario(request, id):
    veterinario= Veterinario.objects.get(id=id)
    if request.method == 'POST':
        veterinario.delete()
        messages.success(request, "Los datos del veterinario fueron eliminados correctamente")
        return redirect('lista-veterinarios')
    return render(request, 'veterinario/eliminar_veterinario.html',{'veterinario':veterinario})

#CRUD DEL MODELO DEL CLIENTE
#TABLA DEL MODELO DE CLIENTE
@login_required(login_url='/login/')
@permission_required('veterinariaapp.view_cliente', raise_exception=True)
def lista_cliente(request):
    clientes= cliente.objects.all()
    return render(request, 'cliente/lista_cliente.html',{'clientes':clientes})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE CLIENTE
@login_required(login_url='/login/')
@permission_required('veterinariaapp.add_cliente', raise_exception=True)
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            email=form.cleaned_data['email']
            nombres=form.cleaned_data['nombres']
            apellidos=form.cleaned_data['apellidos']
            tipo_documento=form.cleaned_data['tipo_documento']
            num_documento=form.cleaned_data['num_documento']
            celular=form.cleaned_data['celular']
            rol=form.cleaned_data['rol']
            cliente=form.save(commit=False)
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
            cliente.persona = persona
            cliente=form.save()
            messages.success(request, "Los datos del veterinario {veterinario} fueron almacenados correctamente")
        else:
            messages.error(request, "Verifique los datos e intente nuevamente")
        return redirect(reverse('lista-clientes'))
    else:
        form = ClienteForm()
        return render(request, 'cliente/crear_cliente.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ACTUALIZAR DEL MODELO DE CLIENTE
@login_required(login_url='/login/')
@permission_required('veterinariaapp.change_cliente', raise_exception=True)
def actualizar_cliente(request, id):
    clientes= cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=clientes)
    else:
        form = ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
        return redirect(reverse('lista-clientes'))
    return render(request, 'cliente/crear_cliente.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ELIMINAR DEL MODELO DE CLIENTE
@login_required(login_url='/login/')
@permission_required('veterinariaapp.delete_cliente', raise_exception=True)
def eliminar_cliente(request, id):
    clientes= cliente.objects.get(id=id)
    if request.method == 'POST':
        clientes.delete()
        messages.success(request, "Los datos del cliente fueron eliminados correctamente")
        return redirect('lista-clientes')
    return render(request, 'cliente/eliminar_cliente.html',{'cliente':clientes})

#CRUD DEL MODELO DEL MASCOTA
#TABLA DEL MODELO DE MASCOTA
@login_required(login_url='/login/')
@permission_required('veterinariaapp.view_mascota', raise_exception=True)
def lista_mascota(request):
    mascota= Mascota.objects.all()
    return render(request, 'mascota/lista_mascota.html',{'mascotas':mascota})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE MASCOTA
@login_required(login_url='/login/')
@permission_required('veterinariaapp.add_mascota', raise_exception=True)
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaFrom(request.POST)
        if form.is_valid():
            form.save()
            print("guardado")
        else:
            print("no guardado")
        return redirect(reverse('lista-mascota'))
    else:
        form= MascotaFrom()
        return render (request,'mascota/crear_mascota.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ACTUALIZAR DEL MODELO DE MASCOTA
@login_required(login_url='/login/')
@permission_required('veterinariaapp.change_mascota', raise_exception=True)
def actualizar_mascota(request,id):
    mascota= Mascota.objects.get(id=id)
    if request.method == 'GET':
        form = MascotaFrom(instance=mascota)
    else:
        form = MascotaFrom(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect(reverse('lista-mascota'))
    return render(request, 'mascota/crear_mascota.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ELIMINAR DEL MODELO DE MASCOTA
@login_required(login_url='/login/')
@permission_required('veterinariaapp.delete_mascota', raise_exception=True)
def eliminar_mascota(request, id):
    mascota= Mascota.objects.get(id=id)
    if request.method == 'POST':
        mascota.delete()
        messages.success(request, "Los datos de la mascota  fueron eliminados correctamente")
        return redirect('lista-mascota')
    return render(request, 'mascota/eliminar_mascota.html',{'mascota':mascota})

#CRUD DEL MODELO DEL REGISTRO
#TABLA DEL MODELO DE REGISTRO
def lista_registro(request):
    registro= Registro.objects.all()
    return render(request, 'registro/lista_registro.html',{'registros':registro})

#LOGICA BASA EN FUNCIONES DE CREAR DEL MODELO DE REGISTRO
@login_required(login_url='/login/')
@permission_required('veterinariaapp.change_registro', raise_exception=True)
def crear_registro(request):
    if request.method == 'POST':
        form= RegistroFrom(request.POST)
        print("requesr valido")
        if form.is_valid():
            registro= form.save()
        else:
            print("no guardo")
            print(form.errors)
        return redirect(reverse('lista-registro'))
    else:
        form= RegistroFrom()
        return render (request,'registro/crear_registro.html',{'form':form})

#LOGICA BASA EN FUNCIONES DE ACTUALIZAR DEL MODELO DE MASCOTA
@login_required(login_url='/login/')
@permission_required('veterinariaapp.change_registro', raise_exception=True)
def actualizar_registro(request,id):
    registro= Registro.objects.get(id=id)
    if request.method == 'GET':
        form = RegistroFrom(instance=registro)
    else:
        form = RegistroFrom(request.POST, instance=registro)
        if form.is_valid():
            form.save()
        return redirect(reverse('lista-registro'))
    return render(request, 'registro/crear_registro.html',{'form':form})

@login_required(login_url='/login/')
@permission_required('veterinariaapp.delete_registro', raise_exception=True)
def eliminar_registro(request, id):
    registro= Registro.objects.get(id=id)
    if request.method == 'POST':
        registro.delete()
        messages.success(request, "Los datos de la mascota  fueron eliminados correctamente")
        return redirect('lista-registro')
    return render(request, 'registro/eliminar_registro.html',{'registro':registro})