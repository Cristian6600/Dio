from django.contrib import admin

from . models import guia, Estado, Motivo, Servicio, tipo

class guiaAdmin(admin.ModelAdmin):

    model = guia
    list_per_page = 12

    list_display = ('Guia', 'Bolsa', 'id_serv', 'id_clie', 'Contiene', 'Orden', 'Domicilio', 'Fecha')
    

admin.site.register(guia, guiaAdmin)
admin.site.register(Estado)
admin.site.register(Motivo)
admin.site.register(Servicio)
admin.site.register(tipo)


