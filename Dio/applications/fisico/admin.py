from django.contrib import admin
from django.db.models.query_utils import FilteredRelation
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import paquete

class paqueteAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('bolsa', 'Seudo', 'Fecha', 'Estado', )

    search_fields = ('bolsa', 'Seudo',)

    list_filter = ('bolsa', 'Seudo', 'Fecha', 'Estado', )

admin.site.register(paquete, paqueteAdmin)



