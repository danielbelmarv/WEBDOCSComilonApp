from django.urls import path
from .views import index, listarPlatos, modificarPlato, pedido, login, registro, agregarPlato

#Solo en debug
from django.conf import settings
from django.conf.urls.static import static
#

urlpatterns = [
    path('', index, name='home'),
    path('pedido/', pedido, name='pedido'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('agregar-plato/', agregarPlato, name='agregar_plato'),
    path('listar-platos/', listarPlatos, name='listar_platos'),
    path('modificar-plato/<id>/', modificarPlato, name='modificar_plato'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)