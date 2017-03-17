from django.conf.urls import url

from .views import VideoListView, VideoDetailView


urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)', VideoDetailView.as_view(), name='detail'),
]