from django.contrib import admin
from .models import Pedido, Plato, Proveedor
from .forms import PlatoForm

# Register your models here.
class platoAdmin(admin.ModelAdmin):
    list_per_page: 8
    form = PlatoForm

admin.site.register(Pedido)
admin.site.register(Plato, platoAdmin)
admin.site.register(Proveedor)