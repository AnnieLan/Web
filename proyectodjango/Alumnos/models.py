from django.db import models

# Create your models here.
class Materia(models.Model):
    materia = models.CharField(max_length = 254,null = False)

class Alumno (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 254,null = False)
    carrera = models.CharField(max_length = 254,null = False)
    edad = models.IntegerField(null = False)
    direccion = models.CharField(max_length = 254,null = False)
    genero = models.CharField(max_length = 254,null = False)
    matricula = models.IntegerField(null = False)
