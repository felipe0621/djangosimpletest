from turtle import title
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=80)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12) 
    
    
class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) #para cuando se borre una personas
                                                                  #se borre tambien la mascota
  
