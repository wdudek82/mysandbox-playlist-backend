from django.db import models
from behaviors.behaviors import Timestamped


class Video(Timestamped):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    embed_code = models.TextField()
    created_at = models.DateTimeField

    def __str__(self):
        return self.title

