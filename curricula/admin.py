from django.contrib import admin
from django import forms
from .models import PublisherGroup, Publisher, LearningMaterial, Curriculum, GradeCurriculum

admin.site.register(PublisherGroup)

admin.site.register(Publisher)


class LearningMaterialAdmin(admin.ModelAdmin):
    search_fields = ['title', 'isbn']

    def queryset(self, request):
        return LearningMaterial.objects.all().prefetch_related('publisher')

admin.site.register(LearningMaterial, LearningMaterialAdmin)

admin.site.register(Curriculum)


class GradeCurriculumAdminForm(forms.ModelForm):
    class Meta:
        model = GradeCurriculum

    def __init__(self, *args, **kwargs):
        super(GradeCurriculumAdminForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['necessary_materials'].queryset = self.instance.materials.all()


class GradeCurriculumAdmin(admin.ModelAdmin):
    form = GradeCurriculumAdminForm
    readonly_fields = ('materials',)
    filter_horizontal = ['necessary_materials']
    search_fields = ['grade_level_start', 'grade_level_end']
    list_display = ('get_parent_name','grade_level_start', 'grade_level_end', 'has_necessary_materials_defined')

admin.site.register(GradeCurriculum, GradeCurriculumAdmin)
