from email.policy import default
from django import forms
from .models import Auditoria

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