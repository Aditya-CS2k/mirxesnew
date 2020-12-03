from django.contrib import admin
from .models import Qualifications, Profile, Departments
# from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Qualifications)
admin.site.register(Profile)
admin.site.register(Departments)


# @admin.register(Qualifications, Profile, Departments)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
