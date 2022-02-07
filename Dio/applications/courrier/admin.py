from django.contrib import admin

from  . models import courrier, vehiculo, Tipo_vehiculo, Marca_vehiculo, Linea_vehiculo, Tipo_infraccion

class courrierAdmin(admin.ModelAdmin):
    icon_name  =  'person_outline'
    raw_id_fields = ["id_ciu",]
    fields = (('d_i', 'courrier'),
            ('cel', 'dir'),('id_ciu','id_veh',),
            ('infraccion', 'licencia',), ('est_courrier'))
    list_filter = ('est_courrier',)
    
admin.site.register(courrier, courrierAdmin)
admin.site.register(vehiculo)
admin.site.register(Tipo_vehiculo)
admin.site.register(Marca_vehiculo)
admin.site.register(Linea_vehiculo)
admin.site.register(Tipo_infraccion)
