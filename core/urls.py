from tabnanny import check
from django.urls import path
from .views import eliminarPlato, index, listarPlatos, modificarPlato, login, registro, agregarPlato, platos, cart, checkout

urlpatterns = [
    path('', index, name='home'),
    path('catalogo/', platos, name='catalogo'),
    path('carrito/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('agregar-plato/', agregarPlato, name='agregar_plato'),
    path('listar-platos/', listarPlatos, name='listar_platos'),
    path('modificar-plato/<id>/', modificarPlato, name='modificar_plato'),
    path('eliminar-plato/<id>/', eliminarPlato, name='eliminar_plato'),
]
