from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('crear/veterinario/', crear_veterinario, name='crear-veterinario'),
    path('listar/veterinario/', lista_veterinario,name='lista-veterinarios'),
    path('borrar/veterinario/<int:id>', borrar_veterinario, name='borrar-veterinario'),
]