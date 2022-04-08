from django.db import models
from django.forms import CharField, IntegerField



# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40, default='Python')
    camada=models.IntegerField(default=0, primary_key=True)


class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(primary_key=True)


class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(primary_key=True)
    profesion=models.CharField(max_length=20)


class Entregable(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    fecha_entregado=models.DateField()
    entregado=models.BooleanField()