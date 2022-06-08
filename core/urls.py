from django.urls import path
from .views import index, pedido, login, registro

urlpatterns = [
    path('', index, name='home'),
    path('pedido/', pedido, name='pedido'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]
