from django.contrib import admin
from django.utils.html import mark_safe
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'embed_code', 'created', 'changed', 'modified']
    list_display_links = ['title']
    readonly_fields = ['created', 'changed', 'modified']
    search_fields = ['title', 'embeded_code']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('title',)}

    def get_embed_code(self, instance):
        return mark_safe(instance.embed_code)
