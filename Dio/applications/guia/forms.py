from django import forms
from .models import guia

class guiafisicoForm(forms.ModelForm):

    class Meta:
        model = guia
        fields = (
            'Bolsa',
            'Seudo'            
        )

    def clean_Seudo(self):
        Seudo = self.cleaned_data['Seudo']
        if len(Seudo) < 22:
            raise forms.ValidationError('Ingrese un codigo de barras correcto')

        return Seudo

    def clean_Bolsa(self):
        Bolsa = self.cleaned_data['Bolsa']
        if len(Bolsa) < 5:
            raise forms.ValidationError('Ingrese codigo de barras correcto')

        return Bolsa