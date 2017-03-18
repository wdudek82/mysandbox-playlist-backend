import random
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Video
from .forms import VideoForm


class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    # success_url = ''


class VideoDetailView(DetailView):
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        return context


class VideoListView(ListView):
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        context['random'] = random.randint(500, 1000)
        return context


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    success_url = '/video/'