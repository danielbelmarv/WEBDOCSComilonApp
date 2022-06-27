from django import forms
from datetime import date
from django.core.validators import MaxValueValidator
from core.validators import MaxSizeFileValidator
from .models import Plato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class PlatoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5, max_length=35)
    precio = forms.IntegerField(min_value=1000, max_value=500000)
    descripcion = forms.CharField(min_length=20, max_length=100)
    fecha_agregado = forms.DateField(validators=[MaxValueValidator(limit_value=date.today)])
    miniatura = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Plato.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError('Ya existe un plato con ese nombre')
        
        return nombre

    class Meta:

        model = Plato
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]