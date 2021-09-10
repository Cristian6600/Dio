from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import User, Profile


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('id', 'username', 'email', 'nombres', 'apellidos', 'genero', 'ciudad')
    search_fields = ('username', 'nombres')

class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
