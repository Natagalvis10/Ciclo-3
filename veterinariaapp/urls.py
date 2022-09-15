from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('crear/veterinario/', crear_veterinario),
    path('listar/veterinario/', lista_veterinario),
    path('borrar/veterinario/<int:id>', borrar_veterinario),
]