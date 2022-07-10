from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    esNuevo = models.BooleanField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha_agregado = models.DateField()
    miniatura = models.ImageField(upload_to='platos', null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
     id_pedido = models.AutoField(primary_key=True)
     cantidad = models.IntegerField()
     precio = models.IntegerField()
     descripcion = models.CharField(max_length=100)
     fecha_pedido = models.DateField()
     estado_pedido = models.CharField(max_length=30)
     
     def __str__(self):
        return self.id_pedido
