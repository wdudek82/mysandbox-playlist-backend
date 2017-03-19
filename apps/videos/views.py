from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Video
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import VideoForm


class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()


class VideoListView(ListView):
    def get_queryset(self):
        queryset = Video.objects.all()
        searched_title = self.request.GET.get('q')
        if searched_title:
            queryset = queryset.filter(title__icontains=searched_title)
        return queryset


class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Video.objects.all()
    success_url = '/video/'
