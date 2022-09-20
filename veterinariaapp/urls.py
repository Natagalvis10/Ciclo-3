from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('listar/veterinario/', lista_veterinario,name='lista-veterinarios'),
    path('crear/veterinario/', crear_veterinario, name='crear-veterinario'),
    path('actualizar/veterinario/<int:id>',actualizar_veterinario , name='actualizar-veterinario'),
    path('eliminar/veterinario/<int:id>', eliminar_veterinario, name='eliminar-veterinario'),
]