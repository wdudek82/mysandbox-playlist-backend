from django.utils.text import slugify


def create_unique_slug(instance, new_slug=None):
    if not new_slug:
        slug = slugify(instance.title)
    else:
        slug = new_slug

    Klass = instance.__class__
    queryset = Klass.objects.filter(slug=slug).order_by('-id')
    if queryset:
        # TODO: Bleh.. there is still a nasty bug here - it won't work with primary slug, and if that primary has
        # hyphen, it will be split in incorrect way - need fix!
        created_slug = slug.rsplit('-')[0] + '-{id_}'.format(id_=queryset.first().id)
        return create_unique_slug(instance, new_slug=created_slug)
    return slug