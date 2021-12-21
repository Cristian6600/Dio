from django import forms
from django.forms import widgets
from .models import Cargue, Recepcion
from applications.guia.models import Guia
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple


class CargueForm(forms.ModelForm):

    class Meta:
        model = Cargue
        fields = (
            'full_name', 
            'guia',
        )

        widgets = {
            'guia': forms.SelectMultiple(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    
                }
            ),
            'full_name': forms.Select(
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
        