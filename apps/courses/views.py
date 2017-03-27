from django.shortcuts import get_object_or_404
from django.db.models import Prefetch, Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from apps.utils.mixins import GetObjectMixin, MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import CourseForm
from .models import Course, Lecture


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


class CourseDetailView(GetObjectMixin, MemberRequiredMixin, DetailView):
    queryset = Course.objects.all()


class CourseUpdateView(GetObjectMixin, StaffMemberRequiredMixin, UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm


class CourseDeleteView(GetObjectMixin, StaffMemberRequiredMixin, DeleteView):
    queryset = Course.objects.all()
    success_url = '/course/'


class LectureDetailView(MemberRequiredMixin, DetailView):
    def get_object(self):
        course_slug = self.kwargs.get('cslug')
        lecture_slug = self.kwargs.get('lslug')
        instance = get_object_or_404(Lecture, course__slug=course_slug, slug=lecture_slug)
        return instance

    # How to get context from generic class based view
    # def get_context_data(self, **kwargs):
    #     context = super(LectureDetailView, self).get_context_data()
    #     print(context)
    #     return context
