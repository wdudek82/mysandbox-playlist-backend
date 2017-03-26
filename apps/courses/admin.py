from django.contrib import admin
from .models import Course, Lecture
from .forms import LectureAdminForm


class LectureInline(admin.TabularInline):
    model = Lecture
    form = LectureAdminForm
    extra = 1
    exclude = ('created', 'modified')
    # raw_id_fields = ['video']
    prepopulated_fields = {'slug': ('title',)}


# TODO: same as in models - maybe better would be to use abstract class to reduce code repetition
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'order', 'category', 'description', 'user', 'is_new', 'price',
                    'created', 'changed', 'modified']
    list_display_links = ['title']
    list_editable = ['order', 'category']
    list_filter = ['user', 'price', 'created', 'modified']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created', 'modified']
    inlines = [
        LectureInline,
    ]


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'order', 'description', 'course', 'video',  'created', 'modified', 'changed']
    list_display_links = ['title']
    list_filter = ['course', 'video', 'created', 'modified']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created', 'modified']
    form = LectureAdminForm
