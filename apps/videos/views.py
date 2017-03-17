import random
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Video


class VideoCreateView(CreateView):
    queryset = Video.objects.all()


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

    # def get(self, request, *args, **kwargs):
    #     print(request.__dict__)
    #     return render(request, self.template_name, '')

    # def post(self, request, *args, **kwargs):
    #     print(request.__dict__)
    #     return render(request, self.template_name, '')


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        return context


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()