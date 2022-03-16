from django import forms
from django.forms import widgets
from .models import Cargue, Planilla, Recepcion
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
        

class AsignarForm(forms.ModelForm):   
    class Meta:
        model = Planilla
        fields = ['full_name', 'guia', 'user']

        widgets = {
            
            'full_name': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            }

    def form_valid(self, form):
        self.object = form.commisave(t=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AsignarForm, self).form_valid(form)    

        
class RecepcionForm(forms.ModelForm):   
    class Meta:
        model = Recepcion
        fields = ['guia', 'estado', 'motivo',]

        widgets = {
            'motivo': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'input-group-field',
                    'readonly': True
                }
            ),
            }

        