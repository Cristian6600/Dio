from django import forms
from .models import Cargue, Recepcion
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _

class CargueForm(forms.ModelForm):

    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model = Cargue
        fields = [
            'id',
            'guia', 
            'mensajero',
        ]

class RecepcionForm(forms.ModelForm):   
    class Meta:
        model = Recepcion
        fields = ['planilla', 'motivo', 'guia', 'bolsa']

        