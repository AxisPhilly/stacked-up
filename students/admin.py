from django.contrib import admin
from .models import Grade, Cohort


class GradeAdmin(admin.ModelAdmin):
    list_display = ('school', 'grade_level')
    list_per_page = 20

admin.site.register(Grade, GradeAdmin)


class CohortAdmin(admin.ModelAdmin):

    def queryset(self, request):
        return Cohort.objects.all().prefetch_related('grade')

    readonly_fields = ('grade',)
    list_display = ('grade', 'year_start', 'year_end',
                    'math_advanced_percent', 'math_proficient_percent',
                    'math_basic_percent', 'math_below_basic_percent',
                    'read_advanced_percent', 'read_proficient_percent',
                    'read_basic_percent', 'read_below_basic_percent',
                    'math_combined_percent')

admin.site.register(Cohort, CohortAdmin)
