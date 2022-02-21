from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import Estado, Motivo, Cod_vis, Nom_producto, Emision, Est_clie

class EmiResource(resources.ModelResource):
    class Meta:
        model = Emision
        import_id_fields = ('t_emi',)

#------------------------------------------------------------------------

@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'Estado',)

@admin.register(Motivo)
class MotivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'motivo', )

@admin.register(Cod_vis)
class MotivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', )

@admin.register(Nom_producto)
class NomproductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Emision)
class emisionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmiResource
    list_display = ('t_emi', 'emision')

@admin.register(Est_clie)
class est_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'estado', 'descripcion', 'proceso', 'cod_est')