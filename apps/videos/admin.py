from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'embed_code', 'created', 'changed', 'modified']
    list_display_links = ['title']
    readonly_fields = ['created', 'changed', 'modified']
    search_fields = ['title', 'embeded_code']
    list_filter = ['created', 'modified']

