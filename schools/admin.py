from django.contrib import admin
from .models import District, SchoolType, School

admin.site.register(District)


class SchoolTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ['approved_curricula']

admin.site.register(SchoolType, SchoolTypeAdmin)


class SchoolAdmin(admin.ModelAdmin):
    filter_horizontal = ['curricula_in_use']

admin.site.register(School, SchoolAdmin)
