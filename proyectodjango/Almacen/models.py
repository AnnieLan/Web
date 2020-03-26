from django.db import models

# Create your models here.

class Almacen(models.Model):
    nombre = models.CharField(max_length = 254,null = False)
    fechaProducto = models.CharField(max_length = 254,null = False)
    FechaCaducidad = models.CharField(max_length = 254,null = False)
    cantidadProducto = models.CharField(max_length = 254,null = False)
    VentasProcuto = models.CharField(max_length = 254,null = False)