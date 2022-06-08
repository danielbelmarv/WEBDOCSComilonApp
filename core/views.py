 
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def pedido(request):
    return render(request, 'core/pedido.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')