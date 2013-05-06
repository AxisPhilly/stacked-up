from .models import SchoolAggregate
from django.views.generic import ListView


class IndexListView(ListView):
    context_object_name = "schools"
    template_name = "index.html"
    model = SchoolAggregate

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        filtered = sorted(SchoolAggregate.objects.all(), key=lambda a: -a.books_for_students())
        context['top_schools'] = filtered[:5]
        context['bottom_schools'] = reversed(filtered[-5:])
        return context
