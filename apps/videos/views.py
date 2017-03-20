from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from apps.utils.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import VideoForm
from .models import Video


class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()


class VideoListView(ListView):
    def get_queryset(self):
        queryset = Video.objects.all()
        searched_video = self.request.GET.get('q')
        if searched_video:
            queryset = queryset.filter(title__icontains=searched_video)
        return queryset


class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Video.objects.all()
    success_url = '/video/'
