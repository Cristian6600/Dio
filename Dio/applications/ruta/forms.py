from django import forms
from django.forms import widgets
from .models import Cargue, Recepcion
from applications.guia.models import Guia
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _

from .models import Programador, Lenguaje

class CargueForm(forms.ModelForm):

    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model = Cargue
        fields = [
            'guia', 
            'mensajero',
        ]
        widgets = {
            'guia': forms.SelectMultiple(
                attrs = {
                    'placeholder': 'Codigo de barras',
                    'class': 'input-group-field',
                }
            ),}
              
# form = CargueForm()
# article = Cargue.objects.get(pk=1)
# form = CargueForm(instance=article)

class RecepcionForm(forms.ModelForm):   
    class Meta:
        model = Recepcion
        fields = ['planilla', 'motivo', 'guia']



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