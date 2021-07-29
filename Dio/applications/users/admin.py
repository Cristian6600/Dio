from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import User

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id', 'username', 'email', 'nombres', 'apellidos', 'genero', 'ciudad')
    search_fields = ('username', 'nombres')

admin.site.register(User, UserAdmin)
