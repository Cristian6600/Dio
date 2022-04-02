from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import datos_g, Orden, Cubrimiento

class CubrimientoResource(resources.ModelResource):
    
    class Meta:
        model = Cubrimiento
        import_id_fields = ('id_cubrimiento',) 

class datos_gResource(resources.ModelResource):
    
    class Meta:
        model = datos_g     
        import_id_fields = ('seudo_dg',)   

##
@admin.register(datos_g)
class datos_gAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = datos_gResource
    list_per_page = 12
    search_fields = ("d_i",)
    list_display = ('seudo_dg', 'direccion', 'd_i', 'id_ciu', 'barrio', 'fecha', )
    icon_name  =  'directions'

@admin.register(Orden)
class ordenAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('orden',)

@admin.register(Cubrimiento)
class CubrimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_cubrimiento', 'oficina', 'direccion', 'dane')
    resource_class = CubrimientoResource


    
