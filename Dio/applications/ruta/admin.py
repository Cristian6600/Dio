from django.contrib import admin

from . models import Cargue, Recepcion

@admin.register(Cargue)
class CargueAdmin(admin.ModelAdmin):
    # fields = (('guia', 'mensajero'),'motivo')
    filter_horizontal = ('guia',)
    list_display = ('id','mensajero', 'fecha',)
    list_editable = ['mensajero']
    search_fields = ('guia',)
    list_filter = ['mensajero__id', 'fecha']
    date_hierarchy = 'fecha'
    list_per_page = 12
    success_url = '.'

@admin.register(Recepcion)
class RecepcionAdmin(admin.ModelAdmin):
    list_display = (
        'id','planilla', 'guia', 'motivo', 'fecha')
    

