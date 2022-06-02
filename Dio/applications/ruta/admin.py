from re import search
from django.contrib import admin
from related_admin import RelatedFieldAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from . models import Cargue, Recepcion, Planilla, Est_planilla, Sucursales, Destino, Descargue
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.text import format_lazy
from applications.fisico.models import Fisico
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources

class PlanillaResource(resources.ModelResource):
    class Meta:
        model = Planilla

        fields = ('guia', 'guia__direccion', 'guia__destinatario', 'guia__id_ciu', 'guia__bolsa', 'full_name__courrier')

        # def export(self, queryset=None, *args, **kwargs):
        #     # For example only export objects with ids in 1, 2, 3 and 4
        #     queryset = queryset and queryset.latest('fecha')
        #     return super(PlanillaResource, self).export(queryset, *args, **kwargs)

class Recepinline (admin.StackedInline):
    model = Fisico
    fields = ('recepcion',)
    raw_id_fields = ["recepcion"]
    
class Planillainline (admin.TabularInline):
    model = Planilla
    extra = 5
    raw_id_fields = ["guia"]

@admin.register(Cargue)
class CargueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    inlines = [Planillainline,]
    save_on_top = False
    # fields = ('id', 'guia'),
    filter_horizontal = ('guia', )
    list_display = ['id', 'fecha',]
    search_fields = ('id', 'full_name__courrier')
    list_filter = ['full_name__id', 'fecha']
    date_hierarchy = 'fecha'
    list_per_page = 12
    success_url = '.'
    icon_name  =  'motorcycle'

@admin.register(Planilla)
class PlanillaAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id','guia', 'full_name',  'fecha', 'user')
    search_fields = ('id', 'guia__id_guia')
    list_filter = ('full_name', 'fecha')
    list_per_page = 10
    date_hierarchy = ('fecha')
    resource_class = PlanillaResource


@admin.register(Recepcion)
class RecepcionAdmin(ImportExportModelAdmin, RelatedFieldAdmin):
    fields = (('motivo'), 'estado', 'guia', 'user')
    # inlines = [Recepinline ,]
    raw_id_fields = ["motivo"]
    list_display = (
        'guia', 'motivo', 'fecha', 'motivo__id', )
    # readonly_fields = ('estado',)
    list_per_page = 10
    search_fields = ('guia__id_guia',)

@admin.register(Est_planilla)
class Est_plaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado')

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'destino', 'fecha', )

admin.site.register(Sucursales)
admin.site.register(Descargue)








    

    

