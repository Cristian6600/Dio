from django.contrib import admin

from  . models import courrier, vehiculo

class courrierAdmin(admin.ModelAdmin):
    autocomplete_fields = ['id_ciu',]

admin.site.register(courrier, courrierAdmin)
admin.site.register(vehiculo)
