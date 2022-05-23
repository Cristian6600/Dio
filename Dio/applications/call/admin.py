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
        fields = (('pregunta_1', 'calificacion_1__calficacion', 
                   'pregunta_2', 'calificacion_2__calficacion',
                   'pregunta_3', 'calificacion_3__calficacion',
                   'pregunta_4', 'calificacion_4__calficacion',
                #    'pregunta_5__pregunta', 'calificacion_5__calficacion',

                   ))

class TelefonoResource(resources.ModelResource):
    
    id = Field (attribute='id', column_name='PSEUDO')
    id__seudo__tarjeta = Field (attribute='id__seudo__tarjeta', column_name='TARJETA')
    id__guia_d_g__marca = Field (attribute='id__guia_d_g__marca', column_name='MARCA')
    id__d_i = Field (attribute='id__d_i', column_name='CEDULA')
    id__destinatario = Field (attribute='id__destinatario', column_name='CLIENTE')
    id__user__ciudad__ciudad = Field (attribute='id__user__ciudad__ciudad', column_name='BODEGA')
    id__id_ciu__ciudad = Field (attribute='id__id_ciu__ciudad', column_name='CIUDAD BASE')
    id__direccion = Field (attribute='id__direccion', column_name='DIRECCION')
    id__mot__motivo = Field (attribute='id__mot__motivo', column_name='RESULTADO')
    id__fecha_recepcion = Field (attribute='id__fecha_recepcion', column_name='FECHA GESTIÓN')
    tel = Field (attribute='tel', column_name='TEL')
    motivo_call = Field (attribute='motivo_call', column_name='ESTADO CALL')
    fecha_call = Field (attribute='fecha_call', column_name='FECHA CALL')
    observacion = Field (attribute='observacion', column_name='OBSERVACIONES')
    user = Field (attribute='user', column_name='ASESOR')
    id__direccion = Field (attribute='id__direccion', column_name='DIRECCION CITA')
    id__id_ciu__ciudad = Field (attribute='id__id_ciu__ciudad', column_name='CIUDAD CITA')
    id__id_ciu__departamento__departamento = Field (attribute='id__id_ciu__departamento__departamento', column_name='DEPARTAMENTO')
    id__proceso__tipo_e = Field (attribute='id__proceso__tipo_e', column_name='TIPO DE ENTREGA')
    OFICINA_CITA = Field(column_name='OFICINA CITA')
    AUTORIZADO = Field(column_name='AUTORIZADO')
    FECHA_AGENDAMIENTO = Field(column_name='FECHA AGENDAMIENTO')
    motivo_call__motivo = Field (attribute='motivo_call__motivo', column_name='TIPIFICACION')
    id__id_est__motivo = Field (attribute='id__id_est__motivo', column_name='ESTADO CUSTODIA')
    

    class Meta:
        model = Telefono
        
        fields = (
            'id', 'id__seudo__tarjeta', 
            'id__guia_d_g__marca', 'id__d_i', 
            'id__destinatario', 'id__user__ciudad__ciudad', 
            'id__id_ciu__ciudad', 'id__direccion', 
            'id__mot__motivo', 'id__fecha_recepcion',
            'tel', 'motivo_call', 'fecha_call', 
            'observacion', 'user', 
            'id__direccion', 'id__id_ciu__ciudad', 
            'id__id_ciu__departamento__departamento', 'id__proceso__tipo_e', 
            'motivo_call__motivo', 'id__id_est__motivo'
        )
        export_order = (
            'id', 'id__seudo__tarjeta', 'id__guia_d_g__marca',
            'id__d_i', 'id__destinatario', 'id__user__ciudad__ciudad',
            'id__id_ciu__ciudad', 'id__direccion', 'id__mot__motivo', 'id__fecha_recepcion',
            'tel', 'motivo_call', 'fecha_call', 'observacion',
            'user', 'id__direccion', 'id__id_ciu__ciudad', 
            'id__id_ciu__departamento__departamento', 
            'id__proceso__tipo_e', 'OFICINA_CITA', 
            'AUTORIZADO', 'FECHA_AGENDAMIENTO',
            'motivo_call__motivo',
        )

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
    list_display = ('id', 'fecha_call' )
    search_fields = ('id',)
    list_filter = ('fecha_call', 'user')
    resource_class = TelefonoResource

class AuditoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    date_hierarchy = ('fecha')
    resource_class = AuditoriaResource
    list_filter  = ('pregunta_1', 'fecha', 'calificacion_1')       
    raw_id_fields = ["entregas",]
    list_display = ('fecha', 'user', 'pregunta_1', 'calificacion_1','pregunta_2', 'calificacion_2', 'pregunta_3', 'calificacion_3', 'pregunta_4', 'calificacion_4')
    fields =(('entregas', ), 
             ('pregunta_1', 'calificacion_1', 'pregunta_2', 'calificacion_2'),
             
             ('pregunta_3', 'calificacion_3', 'pregunta_4', 'calificacion_4'),
             
             ('pregunta_5', 'calificacion_5'),
             'observacion'
             ) 

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()

class PregutasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pregunta', )

admin.site.register(Datos_t, datos_tAdmin)

admin.site.register(Indicativo, IndicativoAdmin)

admin.site.register(Telefono, TelefonoAdmin)

admin.site.register(Pregunta, PregutasAdmin)

admin.site.register(Auditoria, AuditoriaAdmin)

admin.site.register(calificacion)

admin.site.register(Tel)



