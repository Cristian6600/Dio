from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Cliente, Ciudad



class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    
    list_display = ('id_ciu', 'Ciudad', 'dep')
    search_fields = ('id_ciu', 'Ciudad')

admin.site.register(Cliente)
admin.site.register(Ciudad, CiudadAdmin)