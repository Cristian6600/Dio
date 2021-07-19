from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import bd_clie, Producto, est_clie, Emision
# Register your models here.

class bd_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = bd_clie
    list_per_page = 12

    list_display = ('id_clie', 'Archivo', 'Jornada', 'Id_pro', 'D_i', 'Cliente', 'Seudo', 'Id_Proc', 'ofi', 'Canal', 'Realz', 'Tipo', 'D_i_a', 'Codigo', 'id_est_clie', 'orden', 'Bolsa', 'fecha',  'Autor')
    list_filter = ('id_clie', 'fecha' )
    search_fields = ('Archivo', 'Seudo', 'fecha', 'D_i', 'Cliente')

admin.site.register(bd_clie, bd_clieAdmin)
admin.site.register(Producto)
admin.site.register(est_clie)
admin.site.register(Emision)
