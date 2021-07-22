from django.contrib import admin

from . models import Fisico

class fisicoAdmin(admin.ModelAdmin):

    list_display = ('Bolsa', 'Seudo', 'Fecha', 'Estado')

admin.site.register(Fisico, fisicoAdmin)
