from django.http import Http404 
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CustomUserCreationForm, PlatoForm
from core.models import Plato
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

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

@permission_required('core.add_plato')
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

    return render(request, 'core/tools/agregar.html')

@permission_required('core.view_plato')
def listarPlatos(request):

    platos = Plato.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(platos, 5)
        platos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': platos,
        'paginator': paginator
    }

    return render(request, 'core/tools/listar.html')

@permission_required('core.change_producto')
def modificarPlato(request, id):

    plato = get_object_or_404(Plato, id=id)
    data = {
        'form': PlatoForm(instance=plato)
    }

    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST, instance=plato, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='listar_platos')


def eliminarPlato(request, id):
    plato = get_object_or_404(Plato, id=id)
    plato.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to='listar_platos')
