from .models import SchoolAggregate
from schools.models import School
from django.views.generic import ListView
from django.db.models import Q


class IndexListView(ListView):
    context_object_name = "schools"
    template_name = "index.html"
    model = SchoolAggregate

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        filtered = sorted(SchoolAggregate.objects.all(), key=lambda a: -a.books_for_students())
        context['top_schools'] = filtered[:5]
        context['bottom_schools'] = reversed(filtered[-5:])
        context['request'] = self.request
        context['schools'] = School.objects.filter(~Q(schoolaggregate=None))
        return context

class SchoolsListView(ListView):
    context_object_name = "schools"
    template_name = "school_list.html"
    queryset = SchoolAggregate.objects.prefetch_related('school').all().order_by('school')
