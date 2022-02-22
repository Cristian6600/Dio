from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Cliente, Ciudad, Departamento, Oficinas

class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    raw_id_fields = ('departamento',)
    list_display = ('id', 'ciudad', 'departamento', 'cubrimiento')
    search_fields = ('id', 'ciudad')
    list_filter = ('ciudad', 'departamento', 'cubrimiento')
    icon_name  =  'location_city'

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('departamento', )

class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    raw_id_fields = ('id_ciu',)

class OficinasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','direccion')
    search_fields = ('id',)
    list_per_page = 7

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Oficinas, OficinasAdmin)