from django.db import models

# Create your models here.
class Sound(models.Model):
    uri = models.URLField(unique=True, blank=False, primary_key=True) # TODO index? PK?
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.uri, self.title)
