from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from behaviors.behaviors import Timestamped


class Video(Timestamped):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    embed_code = models.TextField()
    free = models.BooleanField(default=True)
    member_required = models.BooleanField(default=False)
    created_at = models.DateTimeField

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video:detail", kwargs={'slug': self.slug})


@receiver(signal=pre_save, sender=Video)
def pre_save_video_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
