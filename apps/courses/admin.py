from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'slug', 'description', 'price', 'created', 'changed', 'modified']
    readonly_fields = ['created', 'modified']
    list_display_link = ['title']
    list_filter = ['user', 'price', 'created', 'modified']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}