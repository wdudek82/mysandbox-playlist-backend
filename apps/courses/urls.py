from django.conf.urls import url
from .views import CourseCreateView, CourseListView


urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='list'),
    url(r'^create/$', CourseCreateView.as_view(), name='create'),
]