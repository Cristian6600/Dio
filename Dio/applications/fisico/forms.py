from django import forms
from .models import Paquete, Fisico

class ProductForm(forms.ModelForm):

    class Meta:
        model = Paquete
        fields = (
            'bolsa',
            'seudo'            
        )

    def clean_Seudo(self):
        Seudo = self.cleaned_data['Seudo']
        if len(Seudo) < 22:
            raise forms.ValidationError('Ingrese un codigo de barras correcto')

        return Seudo

# class FisicoForm(forms.ModelForm):

#     class Meta:
#         model = Fisico
#         fields = ('bolsa', 'seudo')

