from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_documento= models.CharField(max_length=20)
    num_documento= models.CharField(max_length=20)
    dirreccion= models.CharField(max_length=100, blank=True)
    celular= models.CharField(max_length=10)
    
    '''def __str__(self):
        return f"{self.user.firts_name} ({self.user.last_name})"'''

class cliente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    personas=models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.firts_name} ({self.user.last_name})" 

class Veterinario(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    personas=models.ForeignKey(Persona, on_delete=models.CASCADE)
    num_profesional=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user.firts_name} ({self.user.last_name})" 

class Mascota(models.Model):
    cliente=models.ForeignKey(cliente, on_delete=models.CASCADE)
    nobre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    sexo=models.CharField(max_length=20)
    especie=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    edad=models.IntegerField()
    peso=models.FloatField()


class Registro(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario=models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    num_histial=models.IntegerField()
    fecha=models.DateField()
    motivo=models.TextField()
    anamnesicos=models.TextField()
    diagnostico=models.TextField()
    tratamiento=models.TextField()
    