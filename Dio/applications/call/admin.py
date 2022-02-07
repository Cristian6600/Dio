from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from . models import Datos_t, Indicativo, Telefono, Pregunta, Auditoria, calificacion, Tel
from simple_history.admin import SimpleHistoryAdmin
from django.db import transaction


class DatossResource(resources.ModelResource):
    class Meta:
        model = Datos_t
        fields = (('id', 'd_i', 'telefono', 'indicativo', 'activo' ))

class AuditoriaResource(resources.ModelResource):
    class Meta:
        model = Auditoria
        fields = (('pregunta_1__pregunta', 'calificacion_1__calficacion', 
                   'pregunta_2__pregunta', 'calificacion_2__calficacion',
                   'pregunta_3__pregunta', 'calificacion_3__calficacion',
                   'pregunta_4__pregunta', 'calificacion_4__calficacion',
                #    'pregunta_5__pregunta', 'calificacion_5__calficacion',

                   ))
                
class datos_tAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    
    fields = (('d_i', 'telefono',))
    resource_class = DatossResource
    list_per_page = 12
    history_list_display = ["status"]
    list_display = ('telefono', 'activo', 'user', 'd_i')
    SIMPLE_HISTORY_REVERT_DISABLED=True
    raw_id_fields = ["telefono",]
    search_fields = ('d_i',)
    # fields = ('d_i', 'telefono', 'indicativo')

    icon_name  =  'call'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()    

class IndicativoAdmin(admin.ModelAdmin):
    
    list_display = ('ind', 'Region')

class TelefonoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', )
    search_fields = ('id',)

class AuditoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    date_hierarchy = ('fecha')
    resource_class = AuditoriaResource
    list_filter  = ('pregunta_1', 'fecha', 'calificacion_1')       
    raw_id_fields = ["entregas", 'telefono' ]
    list_display = ('fecha', 'user', 'pregunta_1', 'calificacion_1','pregunta_2', 'calificacion_2', 'pregunta_3', 'calificacion_3', 'pregunta_4', 'calificacion_4')
    fields =(('entregas', 'telefono'), 
             ('pregunta_1', 'calificacion_1', 'pregunta_2', 'calificacion_2'),
             
             ('pregunta_3', 'calificacion_3', 'pregunta_4', 'calificacion_4'),
             
             ('pregunta_5', 'calificacion_5'),
             'observacion'
             ) 

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()

admin.site.register(Datos_t, datos_tAdmin)

admin.site.register(Indicativo, IndicativoAdmin)

admin.site.register(Telefono, TelefonoAdmin)

admin.site.register(Pregunta)

admin.site.register(Auditoria, AuditoriaAdmin)

admin.site.register(calificacion)

admin.site.register(Tel)



