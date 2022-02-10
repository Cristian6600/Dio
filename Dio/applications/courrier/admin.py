
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from  . models import courrier, vehiculo, Tipo_vehiculo, Marca_vehiculo, Linea_vehiculo, Tipo_infraccion

class courrierAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name  =  'person_outline'
    raw_id_fields = ["id_ciu",]
    fields = (('d_i', 'courrier'),
            ('cel', 'dir'),('id_ciu','id_veh',),
            ('infraccion', 'licencia',), ('est_courrier'))
    list_filter = ('est_courrier',)
    raw_id_fields = ["id_veh",]
    search_fields = ("d_i", "courrier")
    list_display = ('courrier', 'd_i', 'cel', 'est_courrier')

class VehiculoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_veg', 'name', 'cc', 'marca', 'cilindraje')
  
admin.site.register(courrier, courrierAdmin)
admin.site.register(vehiculo, VehiculoAdmin)
admin.site.register(Tipo_vehiculo)
admin.site.register(Marca_vehiculo)
admin.site.register(Linea_vehiculo)
admin.site.register(Tipo_infraccion)
