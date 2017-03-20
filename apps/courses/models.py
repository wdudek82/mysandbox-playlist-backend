from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from behaviors.behaviors import Timestamped


class Course(Timestamped):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


@receiver(signal=pre_save, sender=Course)
def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
