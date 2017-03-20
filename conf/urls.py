from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Apps
    url(r'^course/', include('apps.courses.urls', namespace='course')),
    url(r'^video/', include('apps.videos.urls', namespace='video')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
