from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Cliente, Ciudad, Departamento

class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    raw_id_fields = ('departamento',)
    list_display = ('id', 'ciudad', 'departamento', 'cubrimiento')
    search_fields = ('id', 'ciudad', 'departamento')
    list_filter = ('ciudad', 'departamento', 'cubrimiento')
    icon_name  =  'location_city'

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('departamento', )

class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    raw_id_fields = ('id_ciu',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)