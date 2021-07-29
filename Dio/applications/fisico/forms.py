from django import forms
from .models import paquete, Fisico

class ProductForm(forms.ModelForm):

    class Meta:
        model = paquete
        fields = (
            'bolsa',
            'Seudo'            
        )

    def clean_Seudo(self):
        Seudo = self.cleaned_data['Seudo']
        if len(Seudo) < 22:
            raise forms.ValidationError('Ingrese un codigo de barras correcto')

        return Seudo

class FisicoForm(forms.ModelForm):

    class Meta:
        model = Fisico
        fields = (
            'Bolsa',
            'Seudo'            
        )
    
    def clean_Seudo(self):
        Seudo = self.cleaned_data['Seudo']
        if len(Seudo) < 22:
            raise forms.ValidationError('Ingrese un codigo de barras correcto')

        return Seudo