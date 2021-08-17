from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import guia, Estado, Motivo, Servicio, tipo
from django.utils.html import format_html

class guiaResource(resources.ModelResource):

    class Meta:
        model = guia
        exclude = ('id_serv')

class guiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = guia
    list_per_page = 12

    list_display = ('id', 'g', 'Fecha', 'Estados', 'id_clie', 'Contiene', 'Orden', 'Domicilio', 'Imagen', 'producto')
    list_filter = ('Fecha', 'producto')

    date_hierarchy = 'Fecha'

class TipoAdmin(admin.ModelAdmin):

    list_display = ('id_tip', 'Tipo')
    
admin.site.register(guia, guiaAdmin)
admin.site.register(Estado)
admin.site.register(Motivo)
admin.site.register(Servicio)
admin.site.register(tipo, TipoAdmin)


