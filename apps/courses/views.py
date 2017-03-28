from django.shortcuts import get_object_or_404, Http404
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView

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
        user = self.request.user
        if searched_course:
            queryset = queryset.filter(
                Q(title__icontains=searched_course) | Q(description__icontains=searched_course))
        if user.is_authenticated():
            queryset = queryset.owned(user)
        return queryset


class CourseDetailView(MemberRequiredMixin, DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        queryset = Course.objects.filter(slug=slug).owned(self.request.user)
        if queryset:
            return queryset.first()
        raise Http404


class CoursePurchaseView(StaffMemberRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, slug=None, *args, **kwargs):
        queryset = Course.objects.filter(slug=slug).owned(self.request.user)
        if queryset:
            user = self.request.user
            if user.is_authenticated():
                my_courses = user.mycourses

                # run transaction
                # if transaction successful:
                my_courses.courses.add(queryset.first())

            return queryset.first().get_absolute_url()
        return '/courses/'


class CourseUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm

    # def get_object(self, queryset=None):
    #     slug = self.kwargs.get('slug')
    #     instance = Course.objects.filter(slug=slug)
    #     if instance:
    #         return instance.first()
    #     raise Http404


class CourseDeleteView(StaffMemberRequiredMixin, DeleteView):
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
