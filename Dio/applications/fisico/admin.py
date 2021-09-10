from django.contrib import admin
from django.db.models.query_utils import FilteredRelation
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import paquete

class paqueteAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    raw_id_fields = ("seudo",)

    list_display = ('bolsa', 'seudo', 'fecha', 'estado', )

    search_fields = ('bolsa', 'Seudo',)

    list_filter = ('bolsa', 'seudo', 'fecha', 'estado', )

    
admin.site.register(paquete, paqueteAdmin)



