from django.contrib import admin
from django.db.models.query_utils import FilteredRelation

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Paquete, Fisico, Bolsa, Mesa
from django.db import models
from django.forms import ModelForm
from django import forms
    
# class MyForm(forms.ModelForm):
#     seudo = forms.CharField(
#         widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
#     class Meta:
#         model = Paquete
#         fields = ('seudo', 'bolsa')
#         labels = {
#             "seudo": "business_center",
        # }        
class PaqueteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # change_form_template = 'admin/fisico/change_form.html'
    # raw_id_fields = ("seudo",)
    fields = (  
        ('bolsa'),
        ('seudo'),
        ('estado'),
        
    )

    list_display = ('seudo', 'bolsa', 'fecha', 'estado')

    search_fields = ('bolsa', 'Seudo',)

    list_filter = ('bolsa', 'seudo', 'fecha', 'estado', )

    # form = MyForm

    icon_name  =  'local_shipping'

class FisicoAdmin(admin.ModelAdmin):
    list_display = ('id_guia', 'bolsa', 'fecha', 'estado')

class BolsaAdmin(admin.ModelAdmin):
    pass

class MesaAdmin(admin.ModelAdmin):
    raw_id_fields = ["guia"]
    list_display = ('guia', 'observacion')

admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(Fisico, FisicoAdmin)
admin.site.register(Bolsa, BolsaAdmin)
admin.site.register(Mesa, MesaAdmin)






