from django.urls import path
from .views import eliminarPlato, index, listarPlatos, modificarPlato, pedido, login, registro, agregarPlato, platos

urlpatterns = [
    path('', index, name='home'),
    path('pedido/', pedido, name='pedido'),
    path('catalogo/', platos, name='catalogo'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('agregar-plato/', agregarPlato, name='agregar_plato'),
    path('listar-platos/', listarPlatos, name='listar_platos'),
    path('modificar-plato/<id>/', modificarPlato, name='modificar_plato'),
    path('eliminar-plato/<id>/', eliminarPlato, name='eliminar_plato'),
]
