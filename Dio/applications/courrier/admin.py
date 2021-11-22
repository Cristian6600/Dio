from django.contrib import admin

from  . models import courrier, vehiculo

class courrierAdmin(admin.ModelAdmin):
    icon_name  =  'person_outline'


admin.site.register(courrier, courrierAdmin)
admin.site.register(vehiculo)
