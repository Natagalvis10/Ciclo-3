from django.urls import path
from .views import *


urlpatterns = [
    #URL DEL HOME PAGE
    path('',home, name='home'),
    #URL DEL LOGIN USER
    path('login/', login_user,name='login'),
    #URL DEL LOGOUT USER
    path('logout/', logout_user,name='logout'),
    #URLS PARA EL MODELO DE ROLES
    path('listar/rol/', listar_rol,name='lista-rol'),
    path('crear/rol/', crear_rol, name='crear-rol'),
    path('eliminar/rol/<int:id>', eliminar_rol, name='eliminar-rol'),
    path('agregar/permisos', agregar_permisos, name='agregar-permiso'),
    #URLS DEL MODELO DE VETERINARIO
    path('listar/veterinario/', lista_veterinario,name='lista-veterinarios'),
    path('crear/veterinario/', crear_veterinario, name='crear-veterinario'),
    path('actualizar/veterinario/<int:id>',actualizar_veterinario , name='actualizar-veterinario'),
    path('eliminar/veterinario/<int:id>', eliminar_veterinario, name='eliminar-veterinario'),
    #URLS DEL MODELO DE CLIENTE
    path('listar/cliente/', lista_cliente,name='lista-clientes'),
    path('crear/cliente/', crear_cliente, name='crear-cliente'),
    path('actualizar/cliente/<int:id>',actualizar_cliente, name='actualizar-cliente'),
    path('eliminar/cliente/<int:id>', eliminar_cliente, name='eliminar-cliente'),
    #URLS DEL MODELO DE MASCOTA
    path('listar/mascota/', lista_mascota, name='lista-mascota'),
    path('crear/mascota/', crear_mascota, name='crear-mascota'),
    path('actualizar/mascota/<int:id>', actualizar_mascota, name='actualizar-mascota'),
    path('eliminar/mascota/<int:id>', eliminar_mascota, name='eliminar-mascota'),
    #URLS DEL MODELO DE REGISTRO
    path('listar/registro/', lista_registro, name='lista-registro'),
    path('crear/registro/', crear_registro, name='crear-registro'),
    path('actualizar/registro/<int:id>', actualizar_registro, name='actualizar-registro'),
    path('eliminar/registro/<int:id>', eliminar_registro, name='eliminar-registro'),
]