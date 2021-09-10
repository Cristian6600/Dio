from django import forms
from .models import paquete

class ProductForm(forms.ModelForm):

    class Meta:
        model = paquete
        fields = (
            'bolsa',
            'seudo'            
        )

    # def clean_Seudo(self):
    #     Seudo = self.cleaned_data['Seudo']
    #     if len(Seudo) < 22:
    #         raise forms.ValidationError('Ingrese un codigo de barras correcto')

    #     return Seudo

