from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import CourseForm
from .models import Course
from apps.utils.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        # int_passed = form.cleaned_data.get('number')
        # Course.objects.create(number=int_passed)
        return super(CourseCreateView, self).form_valid(form)


class CourseListView(ListView):
    def get_queryset(self):
        queryset = Course.objects.all()
        searched_course = self.request.GET.get('q')
        if searched_course:
            queryset = queryset.filter(
                Q(title__icontains=searched_course) | Q(description__icontains=searched_course))
        return queryset


class CourseDetailView(MemberRequiredMixin, DetailView):
    queryset = Course.objects.all()


class CourseUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm


class CourseDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Course.objects.all()
    success_url = '/course/'
