from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import User, Profile

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'nombres', 'apellidos', 'genero', 'ciudad', 'ocupation')
    search_fields = ('username', 'nombres')
    raw_id_fields = ['ciudad']
    list_filter = ('ocupation',)

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

