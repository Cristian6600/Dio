from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import datos_g

class datos_gAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = datos_g
    list_per_page = 12

    list_display = ('Seudo', 'direccion', 'postal', 'id_ciu', 'barrio')

admin.site.register(datos_g, datos_gAdmin)