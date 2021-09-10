from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import guia, Estado, Motivo, Servicio, tipo
from django.utils.html import format_html


from django.contrib.admin.models import LogEntry, ADDITION, CHANGE


from django.contrib.admin import AdminSite
# from simple_history.admin import SimpleHistoryAdmin

admin.site.site_title = 'My site admin'

class guiaResource(resources.ModelResource):
    
    class Meta:
        model = guia
#         import_id_fields = ('id',)
#         fields = ('id', 'bolsa', 'Direccion', 'd_i',)

@admin.register(guia)
class guiaAdmin(ImportExportModelAdmin):
    
    change_list_template = 'admin/guia/guia_change_list.html'
    resource_class = guiaResource
    model = guia
    list_per_page = 12
    fields = (
        
        ('id', 'bolsa'), 
        ('direccion', 'barrio'),
        ('postal', 'id_ciu' ),
        ('id_mot', 'id_pro'),
        ('id_ser','id_clie'),
        ('id_est','producto'),
        ('marca', 'Imagen'),
        ('cantidad', 'fecha') ,
        'user' 
    )

    search_fields = ('id',)
    list_display = ('id', 'bolsa', 'direccion', 'barrio', 'postal', 'id_ciu', 'marca')
    list_filter = ('producto', 'id_ciu',)
    readonly_fields = ('fecha', 'cantidad', 'user')
    actions = None

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user
        obj.save()
    
    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'user', None) is None:
    #         obj.user = request.user
    #         obj.save()

    # date_hierarchy = 'published'

@admin.register(tipo)
class TipoAdmin(admin.ModelAdmin):

    list_display = ('id_tip', 'Tipo')

class MoniterLog(admin.ModelAdmin):
    #dt_utc = datetime.datetime.strptime('action_time', '%Y-%m-%d %H:%M:%S')
    #str_utc = 'action_time'
    #dt_utc = datetime.datetime.strptime(str_utc, '%Y-%m-%d %H:%M:%S')
    #dt_jst =  dt_utc + datetime.timedelta(0,3600)
    #str_jst = dt_jst.strftime('%Y/%m/%d %H:%M:%S') 
    list_display = ('action_time','user','content_type','object_repr','change_message','action_flag')
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

admin.site.register(Estado)
admin.site.register(Motivo)
admin.site.register(Servicio)
admin.site.register(LogEntry, MoniterLog)







