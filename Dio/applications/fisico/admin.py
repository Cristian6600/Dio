from django.contrib import admin
from django.db.models.query_utils import FilteredRelation

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Paquete, Fisico, Bolsa, Mesa, Motivo_mesa, Proceso
from django.db import models
from django.forms import ModelForm
from django import forms
from simple_history.admin import SimpleHistoryAdmin

class FisicoResource(resources.ModelResource):
    
    class Meta:
        model = Fisico
        import_id_fields = ('id_guia',) 
    
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
    
    raw_id_fields = ("seudo",)

    list_display = ('seudo', 'bolsa', 'fecha', 'estado')

    search_fields = ('bolsa', 'Seudo',)

    icon_name  =  'local_shipping'

class FisicoAdmin(SimpleHistoryAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    history_list_display = ["mot", "mensajero"]
    resource_class = FisicoResource
    list_display = ('id_guia', 'bolsa', 'fecha', 'estado', 'mensajero', 'fecha_planilla')
    date_hierarchy = ('fecha_planilla')
    list_filter = ('est_planilla', 'mensajero',)
    
class BolsaAdmin(admin.ModelAdmin):
    pass

class MesaAdmin(admin.ModelAdmin):
    raw_id_fields = ["guia"]
    list_display = ('guia', 'id_motivo_m', 'observacion', )
    search_fields = ('guia__id_guia',)
    list_filter = ("id_motivo_m",)

class ImgAdmin(admin.ModelAdmin):
    list_display = ('id_guia','image')

class ProcesoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(Fisico, FisicoAdmin)
admin.site.register(Bolsa, BolsaAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Motivo_mesa)
admin.site.register(Proceso, ProcesoAdmin)







