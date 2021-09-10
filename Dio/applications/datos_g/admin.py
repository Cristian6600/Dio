from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import datos_g

class datos_gResource(resources.ModelResource):
    
    class Meta:
        model = datos_g     
        import_id_fields = ('seudo')   
        fields = ('seudo', 'bolsa', 'd_i', 'direccion', 'postal', 'id_ciu', 'barrio', 'marca')

class datos_gAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = datos_gResource
    list_per_page = 12
    fields =  (
        ('id', 'bolsa'),
        ('d_i', 'postal'),
        ('direccion', 'id_ciu'),
        ('barrio', 'marca'),
        'id_pro'
        )
    list_display = ('direccion', 'd_i', 'postal', 'id_ciu', 'barrio', 'fecha')

    
admin.site.register(datos_g, datos_gAdmin)