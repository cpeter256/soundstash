import itertools

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

class Sound(models.Model):
    """
    A single sound
    ie, a link and corresponding metadata
    """
    url = models.URLField(blank=False)
    title = models.CharField(max_length=200)
    # optional fields
    artist = models.CharField(max_length=200, blank=True)
    # added_by = models.ForeignKey('User')

    def __str__(self):
        return "%s (%s)" % (self.url, self.title)

class Playlist(models.Model):
    """
    Playlists (a collection of Sounds) and who owns them
    """
    name = models.CharField(max_length=200, default="default")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    sound = models.ManyToManyField(Sound)
    # TODO handle names slugging to same thing
    slug = models.SlugField(editable=False)
    # TODO unique (slug, owner)

    def __str__(self):
        return "%s playlist (owned by %s)" % (self.name, self.owner)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug = slugify(self.name)

            for x in itertools.count(1):
                if not Playlist.objects.filter(owner=self.owner,slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (slug, x)
        super(Playlist, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('name','owner',)
