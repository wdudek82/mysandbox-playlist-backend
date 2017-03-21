from django.utils.text import slugify


def create_unique_slug(instance):
    slug = slugify(instance.title)
    Klass = instance.__class__
    queryset = Klass.objects.filter(slug=slug).order_by('-id')
    if queryset:
        slug = slugify(f'{instance.title}-{queryset[0].id + 1}')
    return slug
