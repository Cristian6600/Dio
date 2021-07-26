from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import guia, Estado, Motivo, Servicio, tipo
from django.utils.html import format_html

class guiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = guia
    list_per_page = 12

    list_display = ('Guia', 'Bolsa', 'id_serv', 'id_clie', 'Contiene', 'Orden', 'Domicilio', 'Fecha', 'Imagen')

    def foto(self, obj):
        return format_html('<img src={} />', obj.Imagen)

class TipoAdmin(admin.ModelAdmin):

    list_display = ('id_tip', 'Tipo')
    
admin.site.register(guia, guiaAdmin)
admin.site.register(Estado)
admin.site.register(Motivo)
admin.site.register(Servicio)
admin.site.register(tipo, TipoAdmin)


