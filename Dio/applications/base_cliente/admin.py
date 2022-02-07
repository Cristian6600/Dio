from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Bd_clie, Producto, Est_clie, Emision
# Register your models here.

class BookResource(resources.ModelResource):
    class Meta:
        model = Bd_clie
        import_id_fields = ('seudo_bd',)

class EmiResource(resources.ModelResource):
    class Meta:
        model = Emision
        import_id_fields = ('t_emi',)

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto
        import_id_fields = ('id_pro',)

class bd_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BookResource
    model = Bd_clie
    list_per_page = 5
    readonly_fields = ('sucursal', 'fe_fisico',)
    list_display = ('seudo_bd', 'guia', 'bolsa', 'jornada', 'cliente', 'fe_fisico', 'id_proc', 'tipo', 'd_i_a', 'id_est_clie')
    list_filter = ('fecha','fecha_recepcion')
    search_fields = ('seudo_bd', 'fecha', 'cliente')
    raw_id_fields = ("id_est_clie",)
    # date_hierarchy = ('fecha_planilla')
    icon_name  =  'cloud_upload'
   
class emisionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmiResource
    list_display = ('t_emi', 'emision')

class productoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductoResource
    list_display = ('id_pro', 'id_clie', 'producto', 'Proceso', 'tipo', 'homologacion')

class est_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id', 'estado', 'descripcion', 'proceso', 'cod_est')

admin.site.register(Bd_clie, bd_clieAdmin)
admin.site.register(Producto, productoAdmin)
admin.site.register(Est_clie, est_clieAdmin)
admin.site.register(Emision, emisionAdmin)

