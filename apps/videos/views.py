from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Video


class VideoCreateView(CreateView):
    queryset = Video.objects.all()


class VideoDetailView(DetailView):
    queryset = Video.objects.all()


class VideoListView(ListView):
    queryset = Video.objects.all()
    template_name = 'videos/video_list.html'
    context = {
        'videos': queryset
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)



class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()