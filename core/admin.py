from django.contrib import admin
from .models import Pedido, Plato, Proovedor

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Plato)
admin.site.register(Proovedor)