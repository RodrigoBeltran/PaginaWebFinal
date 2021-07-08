from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Gabinete, Rams, Juegos, Procesador, GPU


class RamsForm(forms.ModelForm):

    
    class Meta:
        model = Rams
        fields = '__all__'

class JuegosForm(forms.ModelForm):

    
    class Meta:
        model = Juegos
        fields = '__all__'        

class GabineteForm(forms.ModelForm):

    
    class Meta:
        model = Gabinete
        fields = '__all__'   

class ProcesadorForm(forms.ModelForm):
    class Meta:
        model= Procesador
        fields = '__all__'

class GpuForm(forms.ModelForm):

    class Meta:
        model= GPU
        fields= '__all__'