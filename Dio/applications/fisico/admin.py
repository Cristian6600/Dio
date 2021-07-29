from django.contrib import admin
from django.db.models.query_utils import FilteredRelation
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Fisico, paquete

class fisicoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('Bolsa', 'Seudo', 'Fecha', 'Estado', )

    # filter_horizontal = ('Bolsa2',)

    search_fields = ('Bolsa', 'Seudo',)

    list_filter = ('Bolsa', 'Seudo', 'Fecha', 'Estado', )

admin.site.register(Fisico, fisicoAdmin)
admin.site.register(paquete)



