from school_data.models import School, Grade, Cohort, PublisherGroup, Publisher, Textbook, InventoryRecord
from django.contrib import admin

admin.site.register(School)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('school', 'grade_level')
    list_per_page = 20

admin.site.register(Grade, GradeAdmin)


class CohortAdmin(admin.ModelAdmin):
    readonly_fields = ('grade',)
    list_display = ('grade', 'year_start', 'year_end', 'math_advanced_percent', 'math_proficient_percent', 'math_basic_percent', 'math_below_basic_percent', 'read_advanced_percent', 'read_proficient_percent', 'read_basic_percent', 'read_below_basic_percent', 'math_combined_percent')

admin.site.register(Cohort, CohortAdmin)

admin.site.register(Publisher)

admin.site.register(PublisherGroup)

admin.site.register(Textbook)

class InventoryRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('school', 'textbook')

admin.site.register(InventoryRecord, InventoryRecordAdmin)
