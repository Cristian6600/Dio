from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from related_admin import RelatedFieldAdmin
from django.contrib.admin.models import ADDITION, LogEntry, CHANGE
from . models import Servicio, Guia, img
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources

class GuiaResource(resources.ModelResource):
    
    class Meta:
        model = Guia
        import_id_fields = ('seudo',) 
#---------------------------------------------------------

@admin.register(Guia)
class guiaAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, RelatedFieldAdmin):
    history_list_display = ["mot", "fecha_recepcion"]
    resource_class = GuiaResource
    date_hierarchy = ('fecha')
    list_per_page = 5
    raw_id_fields = ["seudo", "mot", "id_est", "cod_vis"]
    fieldsets = [
        (None,  {'fields':[(
            'seudo', 'bolsa', 'destinatario'), 
            ('producto', 'estado', 'id_ciu'), 
            ('direccion', 'barrio', 'postal', ), ]}),

        ('Estados', {'fields':[

            ('id_est', 'mot', 'id_ser',), 
            ('cod_vis', 'id_clie', 'proceso'),
            ('cantidad_vi', 'cantidad', 'codigo', ), ]}) 
    ]
    search_fields = ('id_guia', 'seudo__seudo_bd', 'mot__motivo',)
    list_display = ('id_guia', 'image_mesa__image', 'mot__motivo', 'd_i', 'fecha_recepcion', 'seudo', 'direccion', 'id_ciu', 'fecha', 'user', 'destinatario', 'mensajero', 'estado')
    ordering = ('id_guia',)
    list_filter = ('user', 'id_ciu__departamento','fecha_recepcion', 'mot__motivo',)
    
#     actions = None
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()
    
class MoniterLog(admin.ModelAdmin):
    
    list_display = ('action_time','user','content_type','object_repr','change_message','action_flag')
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

@admin.register(img)
class ImgAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('id_guia', 'image', 'fecha')
    LogEntry.objects.filter(action_flag=ADDITION)
    list_filter = ('fecha',)
    date_hierarchy = ('fecha')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()

admin.site.register(Servicio)
admin.site.register(LogEntry, MoniterLog)



