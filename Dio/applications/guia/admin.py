from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from related_admin import RelatedFieldAdmin
from import_export import resources
from django.contrib.admin.models import ADDITION, LogEntry

from . models import Estado, Servicio, Cod_vis, Guia, img, Feed, FeedFile
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.admin import AdminSite
# from simple_history.admin import SimpleHistoryAdmin

admin.site.site_title = 'My site admin'

class guiaResource(resources.ModelResource):
    
    class Meta:
        model = Guia
        import_id_fields = ('seudo',) 
        fields = ('fecha',  'seudo__cliente', 'seudo__d_i', 'seudo__id_pro__producto', 'id_ciu__ciudad', 'direccion', 'bolsa', 'id_guia', 'postal', 'proceso__proceso', )
        export_order = ('seudo__id_pro__producto', 'seudo__d_i', 'seudo__cliente', 'direccion', 'bolsa', 'id_guia', 'id_ciu__ciudad', 'fecha',  )
@admin.register(Guia)
class guiaAdmin(ImportExportModelAdmin, RelatedFieldAdmin):
    # date_hierarchy = ('fe_entrega')
    list_per_page = 5
    raw_id_fields = ["seudo", "mot", "id_est", "cod_vis"]
    # change_list_template = 'admin/guia/guia_change_list.html'
    resource_class = guiaResource
    fieldsets = [
        (None,  {'fields':[('seudo', 'bolsa', 'destinatario'), ('producto', 'estado', 'id_ciu'), ('direccion', 'barrio', 'postal', ), ]}),
        ('Estados', {'fields':[('id_est', 'mot', 'id_ser',), ('cod_vis', 'id_clie', 'proceso'),
        ('cantidad_vi', 'cantidad', 'codigo', ), 'suma', 'imagen', 'orden' ]}) 
    ]
#     # raw_id_fields = ("mot",)
    search_fields = ('id_guia', 'seudo__seudo_bd', 'mot__motivo',)
    list_display = ('id_guia', 'mot__motivo', 'd_i', 'seudo', 'direccion', 'id_ciu', 'fecha', 'user', 'destinatario', 'imagen')
    ordering = ('id_guia',)
    list_filter = ('user', 'id_ciu__departamento','fecha', 'mot__motivo', 'estado')
#     # readonly_fields = ('fecha', 'cantidad', 'user')
#     actions = None
#     # raw_id_fields = ("id",)

#     icon_name  =  'next_week's
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()
    
    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'user', None) is None:
    #         obj.user = request.user
    #         obj.save()
    # date_hierarchy = 'published'
class MoniterLog(admin.ModelAdmin):
    #dt_utc = datetime.datetime.strptime('action_time', '%Y-%m-%d %H:%M:%S')
    #str_utc = 'action_time'
    #dt_utc = datetime.datetime.strptime(str_utc, '%Y-%m-%d %H:%M:%S')
    #dt_jst =  dt_utc + datetime.timedelta(0,3600)
    #str_jst = dt_jst.strftime('%Y/%m/%d %H:%M:%S') 
    list_display = ('action_time','user','content_type','object_repr','change_message','action_flag')
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

class Cod_visAdmin(ImportExportModelAdmin):
    list_display = ('id', 'visita', 'tipo')

class EstadoAdmin(ImportExportModelAdmin):
    list_display = ('Estado',)

class ImgAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # change_list_template = 'img_change_list.html'
    list_display = ('id_guia', 'image', 'fecha')
    LogEntry.objects.filter(action_flag=ADDITION)
    list_filter = ('fecha',)
    date_hierarchy = ('fecha')
    
    
    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'author', None) is None:
    #         obj.user = request.user 
    #     obj.save()

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Servicio)
admin.site.register(LogEntry, MoniterLog)
admin.site.register(Cod_vis, Cod_visAdmin)

admin.site.register(img, ImgAdmin)
admin.site.register(Feed)
admin.site.register(FeedFile)

