from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import datos_t, indicativo
from simple_history.admin import SimpleHistoryAdmin

class datos_tAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    model = datos_t
    list_per_page = 12
    history_list_display = ["status"]

    list_display = ('telefono', 'indicativo', 'id_mot', 'Activo')
    SIMPLE_HISTORY_REVERT_DISABLED=True

class IndicativoAdmin(admin.ModelAdmin):
    
    list_display = ('ind', 'Region')

admin.site.register(datos_t, datos_tAdmin)

admin.site.register(indicativo, IndicativoAdmin)
