from django import forms
from .models import guia

class guiafisicoForm(forms.ModelForm):

    class Meta:
        model = guia
        fields = (
            'bolsa',
            'Seudo'            
        )

    def clean_Bolsa(self):
        bolsa = self.cleaned_data['bolsa']
        if len(bolsa) < 5:
            raise forms.ValidationError('Ingrese codigo de barras correcto')

        return bolsa

        

#     def clean_Seudo(self):
#         Seudo = self.cleaned_data['Seudo']
#         if len(Seudo) < 22:
#             raise forms.ValidationError('Ingrese un codigo de barras correcto')

#         return Seudo

    