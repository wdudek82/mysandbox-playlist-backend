from django import forms
from .models import Course, Lecture, Video


class LectureAdminForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['order', 'title', 'slug', 'video', 'description']

    def __init__(self, *args, **kwargs):
        super(LectureAdminForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = 'Test initial title'

        instance = kwargs.get('instance')
        qs = Video.objects.filter(lecture__isnull=True)

        # Limit choices to videos not connected by fk to any other lecture
        if instance and instance.video:
            this_ = Video.objects.filter(pk=instance.video.pk)
            # union
            qs = (qs | this_)
            self.fields['video'].queryset = qs
        else:
            self.fields['video'].queryset = qs



class CourseForm(forms.ModelForm):
    # number = forms.IntegerField()

    class Meta:
        model = Course
        fields = ['title', 'slug', 'description', 'price']

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        queryset = Course.objects.filter(slug=slug)
        if queryset.count() > 1:
            raise forms.ValidationError('Slug must be unique!')