from django.db.models import Q
from django.views.generic import CreateView, ListView

from .forms import CourseForm
from .models import Course
from apps.utils.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseListView(ListView):
    def get_queryset(self):git
        queryset = Course.objects.all()
        searched_course = self.request.GET.get('q')
        if searched_course:
            queryset = queryset.filter(
                Q(title__icontains=searched_course) | Q(description__icontains=searched_course))
        return queryset