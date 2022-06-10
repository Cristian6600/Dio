from dataclasses import field
from django.contrib import admin
from django.db.models.query_utils import FilteredRelation
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Paquete, Fisico, Bolsa, Mesa, Motivo_mesa, Cobertura
from simple_history.admin import SimpleHistoryAdmin

class FisicoResource(resources.ModelResource):
    class Meta:
        model = Fisico
        import_id_fields = ('id_guia',) 
        fields = ("id_guia", "destinatario", "d_i", "proceso__proceso", "estado_img", "image_mesa__fecha")
        
class BolsaResource(resources.ModelResource):
    class Meta:
        model = Bolsa
        
class CoberturaResource(resources.ModelResource):
    class Meta:
        model = Cobertura
        import_id_fields = ('bolsa',)
        exclude = ('user',)
#--------------------------------------------------------------------
@admin.register(Paquete)    
class PaqueteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ('fecha',)
    raw_id_fields = ("seudo",)
    list_display = ('seudo', 'bolsa', 'fecha', 'estado')
    search_fields = ('bolsa__bolsa', )
    icon_name  =  'local_shipping'
    list_per_page = 5

@admin.register(Fisico)
class FisicoAdmin(SimpleHistoryAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    history_list_display = ["mot", "mensajero"]
    resource_class = FisicoResource
    list_display = ('id_guia', 'bolsa', 'fecha', 'estado', 'mensajero', 'fecha_planilla')
    date_hierarchy = ('fecha_planilla')
    list_filter = ('est_planilla', 'mensajero', 'estado_img')
    search_fields = ('bolsa', )
    list_per_page = 5
    raw_id_fields = ['id_ciu',]

@admin.register(Bolsa)    
class BolsaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    search_fields = ('bolsa',)
    resource_class = BolsaResource
    list_per_page = 5

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    raw_id_fields = ["guia"]
    list_display = ('guia', 'id_motivo_m', 'observacion', )
    search_fields = ('guia__id_guia',)
    list_filter = ("id_motivo_m",)
    list_per_page = 5

@admin.register(Cobertura)
class CoberturaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CoberturaResource
    date_hierarchy = ('fecha')
    list_display = ('bolsa', 'fecha')
    list_per_page = 5
    search_fields = ('bolsa__bolsa',)
    raw_id_fields = ['bolsa',]
    

admin.site.register(Motivo_mesa)








