from django.db import models
from django.conf import settings

# not sure about my PK choices

class Sound(models.Model):
    """
    A single sound
    ie, a link and corresponding metadata
    """
    url = models.URLField(blank=False) # TODO index? PK?
    title = models.CharField(max_length=200)
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
    def __str__(self):
        return "%s playlist belonging to %s" % (self.name, self.owner)

    # "Masterlist" of all stashed sounds & their corresponding libraries
# TODO on-delete behaviour also rename this
class Masterlist(models.Model):
    sound = models.ManyToManyField(Sound)
    library = models.ManyToManyField(Playlist)
    class Meta:
        verbose_name_plural = "Masterlist"
