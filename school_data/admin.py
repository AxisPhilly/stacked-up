from school_data.models import School, Grade, Cohort
from django.contrib import admin

admin.site.register(School)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('school', 'grade_level')
    list_per_page = 2000

admin.site.register(Grade, GradeAdmin)


class CohortAdmin(admin.ModelAdmin):
    list_display = ('grade', 'year_start', 'year_end')

admin.site.register(Cohort, CohortAdmin)
