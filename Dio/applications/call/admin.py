from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from . models import Datos_t, Indicativo, Telefono
from simple_history.admin import SimpleHistoryAdmin
from django.db import transaction

class DatossResource(resources.ModelResource):
    class Meta:
        model = Datos_t
        fields = ('id', 'd_i', 'telefono', 'indicativo', 'activo' )

class datos_tAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = DatossResource
    list_per_page = 12
    history_list_display = ["status"]
    list_display = ('telefono', 'activo', 'user',)
    SIMPLE_HISTORY_REVERT_DISABLED=True
    raw_id_fields = ["telefono",]
    # fields = ('d_i', 'telefono', 'indicativo')

    icon_name  =  'call'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()    

class IndicativoAdmin(admin.ModelAdmin):
    
    list_display = ('ind', 'Region')

class TelefonoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cc', 'tel')
    search_fields = ('cc',)

admin.site.register(Datos_t, datos_tAdmin)

admin.site.register(Indicativo, IndicativoAdmin)

admin.site.register(Telefono, TelefonoAdmin)



