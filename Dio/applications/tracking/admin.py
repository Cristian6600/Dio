from django.contrib import admin
from . models import Rastreo
from related_admin import RelatedFieldAdmin

@admin.register(Rastreo)
class PdfCobertura(admin.ModelAdmin):
    list_display = ('id', 'id_guia', 'fecha', 'motivopr', 'estado')
    search_fields = ('id', 'id_guia__id_guia' , 'id_fisico_track__id_guia')

    