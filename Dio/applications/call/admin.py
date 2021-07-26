from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import datos_t, indicativo

class datos_tAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = datos_t
    list_per_page = 12

    list_display = ('telefono', 'indicativo', 'id_mot', 'Activo')

class IndicativoAdmin(admin.ModelAdmin):
    
    list_display = ('ind', 'Region')

admin.site.register(datos_t, datos_tAdmin)
admin.site.register(indicativo)
