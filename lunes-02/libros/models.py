from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
    genero=models.CharField(max_length=10)
    fecha_publicacion=models.DateField