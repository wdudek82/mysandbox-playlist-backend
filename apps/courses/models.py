from datetime import datetime, timedelta
import moneyed

import pytz
from behaviors.behaviors import Timestamped
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from djmoney.models.fields import MoneyField

from apps.utils.create_unique_slug import create_unique_slug
from apps.utils.position_field import PositionField
from apps.videos.models import Video


class Course(Timestamped):
    POSITION = (
        ('main', 'main'),
        ('secondary', 'secondary'),
    )

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    order = PositionField(collection='category')
    category = models.CharField(max_length=9, choices=POSITION, default='main')
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

    class Meta:
        ordering = ['category', 'order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:detail', kwargs={'slug': self.slug})

    def is_new(self):
        now = datetime.now(pytz.utc)
        is_current = self.created <= now
        is_recent = self.created >= now - timedelta(days=5)
        return True if is_current and is_recent else False


class MyCourses(Timestamped):
    user = models.OneToOneField(User)
    courses = models.ManyToManyField(Course, blank=True, related_name='owned_by')

    class Meta:
        verbose_name_plural = 'My Courses'

    def __str__(self):
        return str(self.courses.all().count())


@receiver(post_save, sender=User)
def post_save_user_create(sender, instance, created, *args, **kwargs):
    if created:
        MyCourses.objects.get_or_create(user=instance)
# post_save.connect(post_save_user_create, sender=User)


# TODO: I guess it's too much repetition - I'll try to use abstract class for videos, courses, and lectured
# TODO: create app abstrac_classes (?)
class Lecture(Timestamped):
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.SET_NULL)  # limit_choices_to={'lecture__isnull': True}

    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, help_text='Some help text for slug field')
    order = PositionField(collection='course')
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('slug', 'course'),)
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:lecture_detail',
                       kwargs={
                           'cslug': self.course.slug,
                           'lslug': self.slug
                       })


@receiver(signal=pre_save, sender=Course)
@receiver(signal=pre_save, sender=Lecture)
def pre_save_course_receiver(sender, instance, *args, **kwargs):
    queryset = Course.objects.filter(slug=instance.slug)
    if not instance.slug or queryset.count() > 1:
        instance.slug = create_unique_slug(instance)
