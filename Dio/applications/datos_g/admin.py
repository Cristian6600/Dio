from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Tipo, Motivo, datos_g

class datos_gResource(resources.ModelResource):
    
    class Meta:
        model = datos_g     
        import_id_fields = ('seudo_dg',)   
        # fields = ('seudo', 'd_i', 'direccion', 'postal', 'id_ciu', 'barrio', 'marca')

@admin.register(datos_g)
class datos_gAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = datos_gResource
    list_per_page = 8
    list_per_page = 12
    # fields =  (
    #     ('id',),
    #     ('d_i', 'id_ciu'),
    #     ('direccion', 'postal' ),
    #     ('barrio', 'marca'),
    #     ('id_pro', 'mot')
    #     )
    list_display = ('direccion', 'd_i', 'id_ciu', 'barrio', 'fecha', )

    icon_name  =  'directions'

@admin.register(Motivo)
class MotivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id', 'motivo', 'id_tip')
    
