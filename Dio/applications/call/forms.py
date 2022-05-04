from email.policy import default
from django import forms
from .models import Auditoria
from applications.guia.models import Guia
from applications.argumento.models import Motivo, Cod_vis
from applications.cliente.models import Ciudad
from django.db.models import Q
class CallfisicoForm(forms.ModelForm):
    
    class Meta:
        model = Auditoria
        fields = (
            '__all__'
        )

        widgets = {
            'entregas': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                    
                }
            ),

            'pregunta_1': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'calificacion_1': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    'width': 1100
                }
            ),
            'pregunta_2': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'calificacion_2': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'pregunta_3': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'calificacion_3': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'pregunta_4': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'calificacion_4': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'pregunta_5': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'calificacion_5': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'observacion': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            
            

        }
class guiafisicoForm(forms.ModelForm):
    
    class Meta:
        model = Guia
        fields = (
            'id_guia',
            'bolsa',
            'seudo',   
            'user',   
        )

class CallUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CallUpdateForm, self).__init__(*args, **kwargs)
        self.fields['id_ciu'].queryset = Ciudad.objects.filter(cubrimiento = "COBERTURA")
        self.fields['mot'].queryset = Motivo.objects.filter(Q (id = 19)|Q(id = 20))
        self.fields['cod_vis'].queryset = Cod_vis.objects.filter(
            Q (id = 21)|Q(id = 22)|Q(id = 23)|Q(id = 24)|Q(id = 25)
            |Q(id = 26)|Q(id = 27)|Q(id = 28)|Q(id = 29)|Q(id = 30)
            |Q(id = 31)|Q(id = 32)|Q(id = 33)|Q(id = 34)|Q(id = 35)
            )
    
    class Meta:
        model = Guia
        fields = (
            'direccion',
            'id_ciu',
            'postal',
            'mot',
            'cod_vis',
            'motivo_call',
            'oficina',
            'proceso',
            
        )

        widgets = {
            'direccion': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    
                }
            ),
            'postal': forms.TextInput(
                attrs = {
                    'placeholder': 'Postal',
                    'class': 'input-group-field',         
                    
                }
            ),
            'id_ciu': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'mot': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                       
                }
            ),
            'cod_vis': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'motivo_call': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                      
                }
            ),
            'oficina': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'proceso': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            

}

