from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Cliente, Ciudad

class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    
    list_display = ('id', 'Ciudad', 'dep', 'Cubrimiento')
    search_fields = ('id', 'Ciudad', 'dep')
    list_filter = ('Ciudad', 'dep', 'Cubrimiento')

admin.site.register(Cliente)
admin.site.register(Ciudad, CiudadAdmin)