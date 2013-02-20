from school_data.models import School, Grade
from django.contrib import admin

admin.site.register(School)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('school', 'grade_level')

admin.site.register(Grade, GradeAdmin)
