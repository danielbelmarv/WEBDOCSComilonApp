from django.http import Http404 
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CustomUserCreationForm, PlatoForm
from core.models import Plato
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def pedido(request):
    return render(request, 'core/pedido.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Tu registro se ha completado correctamente')
            return redirect(to='home')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)

def agregarPlato(request):
    data = {
        'form': PlatoForm()
    }

    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado correctamente'
        else:
            data['form'] = formulario

    return render(request, 'core/tools/agregar.html', data)

def listarPlatos(request):
    platos = Plato.objects.all()

    data = {
        'platos': platos
    }
    
    return render(request, 'core/tools/listar.html', data)

def modificarPlato(request, id):
    


    return render(request, 'core/tools/modificar.html')