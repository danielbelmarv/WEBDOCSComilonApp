from django.urls import path
from .views import index, pedido, login, registro

#Solo en debug
from django.conf import settings
from django.conf.urls.static import static
#

urlpatterns = [
    path('', index, name='home'),
    path('pedido/', pedido, name='pedido'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)