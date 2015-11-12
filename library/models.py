from django.db import models

# not sure about my PK choices

# Create your models here.
class Sound(models.Model):
    url = models.URLField(unique=True, blank=False, primary_key=True) # TODO index? PK?
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.uri, self.title)

class User(models.Model):
    userid = models.CharField(max_length=200, unique=True, primary_key=True) # pk??
    sounds = models.ManyToManyField(Sound)
    def __str__(self):
        return str(self.userid)

