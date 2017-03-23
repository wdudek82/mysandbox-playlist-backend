from behaviors.behaviors import Timestamped
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.videos.models import Video
from apps.utils.create_unique_slug import create_unique_slug


class Course(Timestamped):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:detail', kwargs={'slug': self.slug})


# TODO: I guess it's too much repetition - I'll try to use abstract class for videos, courses, and lectured
# TODO: create app abstrac_classes (?)
class Lecture(Timestamped):
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, help_text='Some help text for slug field')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture:detail', kwargs={'slug': self.slug})


@receiver(signal=pre_save, sender=Course)
@receiver(signal=pre_save, sender=Lecture)
def pre_save_course_receiver(sender, instance, *args, **kwargs):
    queryset = Course.objects.filter(slug=instance.slug)
    if not instance.slug or queryset.count() > 1:
        instance.slug = create_unique_slug(instance)
