from django.contrib import admin
from related_admin import RelatedFieldAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from . models import Cargue, Recepcion, Planilla, Recep_guia
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.text import format_lazy
from applications.fisico.models import Fisico

from django import forms

# class MyForm(forms.ModelForm):
#     pass

class Recepinline (admin.StackedInline):
    model = Fisico
    fields = ('recepcion',)
    raw_id_fields = ["recepcion"]
    
class Planillainline (admin.StackedInline):
    model = Planilla
    extra = 4
    raw_id_fields = ["guia"]

class PlanillaResource(resources.ModelResource):
#     published = Field(attribute='guia__seudo__direccion', column_name='planilla')
    # publisheds = Field(attribute='guia__id_ciu__ciudad', column_name='Ciudad')
    # publishedss = Field(attribute='guia__direccion', column_name='Direccion')
    # publishedsss = Field(attribute='cargue__mensajero__courrier', column_name='Mensajero')
    class Meta:
        model = Planilla
        fields = (
            'guia', 'guia__direccion', 'guia__id_ciu__ciudad', 'guia__fecha', 'guia__proceso__proceso', 'guia__destinatario', 'guia__d_i', 'cargue__fecha')
        export_order = ('guia__d_i', 'guia__destinatario', 'guia__direccion', 'guia', 'guia__proceso__proceso', 'guia__id_ciu__ciudad', 'guia__fecha', 'cargue__fecha')
        
# class MyForm(forms.ModelForm):

#     class Meta:
#         model = Cargue
#         fields = ('mensajero',)

@admin.register(Cargue)
class CargueAdmin(admin.ModelAdmin):
    
    # change_list_template = 'admin/ruta/Cargue/ruta_change_form.html'
    inlines = [Planillainline,]
    save_on_top = False
    # fields = ('id', 'guia'),
    filter_horizontal = ('guia', )
    list_display = ['id','mensajero', 'fecha',]
    list_editable = ['mensajero']
    search_fields = ('id', 'mensajero__courrier')
    list_filter = ['mensajero__id', 'fecha']
    date_hierarchy = 'fecha'
    list_per_page = 12
    success_url = '.'
    # form = MyForm
    icon_name  =  'motorcycle'

    
@admin.register(Planilla)
class PlanillaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PlanillaResource
    list_display = ('guia', 'cargue',)
    search_fields = ('id',)

# class  Recep_Guiainline (admin.StackedInline):
#     model = Recep_guia
#     extra = 1
    
# @admin.register(Recep_guia)
# class Recep_GuiaAdmin(admin.ModelAdmin):
#     pass

@admin.register(Recepcion)
class RecepcionAdmin(RelatedFieldAdmin):
    fields = (('planilla', 'motivo'), 'estado', 'guia')
    # inlines = [Recepinline ,]
    raw_id_fields = ["motivo"]
    # filter_vertical = ('guia',) 
    list_display = (
        'guia','planilla', 'motivo', 'fecha', 'motivo__id', )

    # readonly_fields = ('estado',)
    # search_fields = ['Recepinline',]
    # list_editable = ('motivo',)
    # list_filter = ('fecha',)
    # raw_id_fields = ("motivo",)

@admin.register(Recep_guia)
class Recep_guiaAdmin(admin.ModelAdmin):
    pass



    

    

