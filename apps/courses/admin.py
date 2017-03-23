from django.contrib import admin
from .models import Course, Lecture


class LectureInline(admin.TabularInline):
    model = Lecture
    extra = 1
    exclude = ('created', 'modified')


# TODO: same as in models - maybe better would be to use abstract class to reduce code repetition
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'slug', 'description', 'price', 'created', 'changed', 'modified']
    readonly_fields = ['created', 'modified']
    list_display_link = ['title']
    list_filter = ['user', 'price', 'created', 'modified']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        LectureInline,
    ]


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'description', 'course', 'video',  'created', 'modified', 'changed']
    readonly_fields = ['created', 'modified']
    list_display_links = ['title']
    list_filter = ['course', 'video', 'created', 'modified']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
