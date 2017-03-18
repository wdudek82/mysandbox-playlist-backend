from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Video
from .forms import VideoForm


class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm


class VideoDetailView(DetailView):
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        return context


class VideoListView(ListView):
    def get_queryset(self):
        queryset = Video.objects.all()
        searched_title = self.request.GET.get('q')
        if searched_title:
            queryset = queryset.filter(title__icontains=searched_title)
        return queryset


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    success_url = '/video/'