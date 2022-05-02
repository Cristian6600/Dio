from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Bd_clie

#####funcion eliminar toda la data 
def Actualizar(modeladmin, request, queryset):
    queryset.update(jornada='AM')

class BdResource(resources.ModelResource):
    class Meta:
        model = Bd_clie
        import_id_fields = ('seudo_bd',)
        
#----------------------------------------------------
@admin.register(Bd_clie)
class bd_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = [Actualizar]
    resource_class = BdResource
    model = Bd_clie
    list_per_page = 5
    readonly_fields = ('sucursal',)
    list_display = ('seudo_bd', 'jornada', 'tipo',  'id_est_clie')
    list_filter = ('fecha', 'fisicos')
    search_fields = ('seudo_bd',)
    raw_id_fields = ("id_est_clie",)
    icon_name  =  'cloud_upload'
   



