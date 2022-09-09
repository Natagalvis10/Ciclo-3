from django.contrib import admin
from veterinariaapp import *
from veterinariaapp.models import Mascota, Persona, Registro, Veterinario, cliente

admin.site.register(Persona)
admin.site.register(cliente)
admin.site.register(Veterinario)
admin.site.register(Mascota)
admin.site.register(Registro)

