from django import forms
from django.forms import widgets
from .models import Cargue, Recepcion
from applications.guia.models import Guia
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Programador, Lenguaje

class CargueForm(forms.ModelForm):

    class Meta:
        model = Cargue
        fields = (
            'mensajero', 
            'guia',
        )

        widgets = {
            'guia': forms.SelectMultiple(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    
                }
            ),
            'mensajero': forms.Select(
                attrs = {
                'class': 'input-group-field',
                }
            ),
            }
        
              
# form = CargueForm()
# article = Cargue.objects.get(pk=1)
# form = CargueForm(instance=article)

class RecepcionForm(forms.ModelForm):   
    class Meta:
        model = Recepcion
        fields = ['planilla', 'motivo', 'guia', 'estado']

        widgets={
            'planilla': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'motivo': forms.Select(
                attrs = {
                'class': 'input-group-field',
                }
            ),
            'estado': forms.Select(
                attrs= {
                    'class': 'input-group-field',
                }
            ),
            'guia': forms.NumberInput(
                attrs = {
                    'placeholder': 'Barcode guia',
                    'class': 'input-group-field',
                    'autofocus': 'autofocus'  ,
                    'class': 'input-group-field',
                    'size': '10'
                }
            ),
                
            }
        
        

class ProgramadorForm(forms.ModelForm):
    """  formulario para seleccionar autores """

    languages = forms.ModelMultipleChoiceField(
        queryset=Lenguaje.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Programador
        fields = (
            'full_name',
            'ocupation',
            'age',
            'languages',
        )
        widgets = {
            'full_name': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombres..',
                    'class': 'form-control',
                }
            ),
            'ocupation': forms.TextInput(
                attrs = {
                    'placeholder': 'Ocupacion..',
                    'class': 'form-control',
                }
            ),
            'age': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }