from django.test import TestCase, Client

from django.contrib.auth.models import User
from .models import Playlist, Sound

# Create your tests here.
class PlaylistTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')

    def test_playlist(self):
        n = len(Playlist.objects.filter(owner=self.user))
        self.assertEqual(n, 0)
        # create playlist
        p = Playlist(name='testplaylist',owner=self.user)
        p.save()
        n = len(Playlist.objects.filter(owner=self.user))
        self.assertEqual(n,1)
        # add songs to playlist
        s1 = Sound(url='https://www.youtube.com/watch?v=JGhoLcsr8GA',
                   artist='Macklemore & Ryan Lewis',
                   title='Downtown')
        s2 = Sound(url='https://www.youtube.com/watch?v=YQHsXMglC9A',
                   artist='Adele',
                   title='Hello')
        s1.save()
        s2.save()
        p.sound.add(s1)
        p.sound.add(s2)
        n = len(Sound.objects.filter(playlist=p,playlist__owner=self.user))
        self.assertEqual(n, 2)
        # delete playlist
        p.delete()
        n = len(Playlist.objects.filter(owner=self.user))
        self.assertEqual(n, 0)
        """
        When we delete a playlist, all songs on it
        should also be deleted
        """
        n = len(Sound.objects.filter(playlist__owner=self.user))
        self.assertEqual(n, 0)
