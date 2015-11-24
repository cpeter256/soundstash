from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

from .forms import AddSongForm
from .models import Sound, Playlist

import json

@login_required
def index(request):
    return render_to_response('index.html')

def register(request):
    return render_to_response('registration.html')

@login_required
def playlist(request):
    """
    Display "playlist" page with songs
    """
    return render_to_response('index.html')

@login_required
def playlist_view(request, playlist='default'):
    if (request.method == 'POST'):
        # TODO handle failures
        artist = request.POST['artist']
        title = request.POST['title']
        url = request.POST['url']
        s = Sound(url=url, title=title, artist=artist)
        s.save()
        # TODO handle nonexistant playlist
        p = Playlist.objects.get(owner=request.user,
                                 slug=playlist)
        p.sound.add(s)
        p.save()
        return HttpResponse()
    else:
        return render_to_response('index.html')

# TODO maybe move this fn to another file?
@login_required
def list_of_playlists(request):
    """
    Return a list of all playlists owned by user
    when an HTTP request is made to /playlists/all
    """
    playlists = Playlist.objects.filter(owner=request.user).values('name')
    return HttpResponse(json.dumps(list(playlists)), content_type='application/json')
