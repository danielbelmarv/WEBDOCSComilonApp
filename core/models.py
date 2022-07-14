from hashlib import blake2b
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from numpy import ones

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

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True)
    correo = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
     id_pedido = models.AutoField(primary_key=True)
     precio = models.IntegerField()
     fecha_pedido = models.DateField()
     estado_pedido = models.BooleanField(default=False, null=True, blank=True)
     id_transaccion = models.CharField(max_length=100, null=True)
     usuario = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True, blank=True)
     
     def __str__(self):
        return str(self.id_pedido)

class DetallePedido(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateField()

class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, null=True)
    direccion = models.CharField(max_length=70, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    comuna = models.CharField(max_length=50, null=False)
    codigo_postal = models.CharField(max_length=20, null=False)
    fecha_agregado = models.DateField()

    def __str__(self):
        return self.direccion