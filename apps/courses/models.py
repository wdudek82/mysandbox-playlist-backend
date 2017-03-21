from behaviors.behaviors import Timestamped
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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


@receiver(signal=pre_save, sender=Course)
def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)
