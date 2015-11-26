from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

from .forms import AddSongForm
from .models import Sound, Playlist

import json

@login_required
def index(request):
    return render_to_response('index.html')

@login_required
def playlist_view(request, playlist='default'):
    if (request.method == 'POST'):
        # TODO handle failures
        artist = request.POST['artist']
        title = request.POST['title']
        url = request.POST['url']
        # TODO want to check if user has this song in another playlist
        # and re-use it if they do!
        # BUT don't want to share song objs amongst users...
        # what if one user edits the song info? it would change for everyone else
        s = Sound(url=url, title=title, artist=artist)
        s.save()
        # TODO handle nonexistant playlist
        p = Playlist.objects.get(owner=request.user,
                                 slug=playlist)
        p.sound.add(s)
        p.save()
        return HttpResponse()
    elif (request.method == 'DELETE'):
        # TODO check for existence
        try:
            p = Playlist.objects.get(owner=request.user,
                                 slug=playlist)
            songs = Sound.objects.filter(playlist=p)
            # TODO both these deletes are necessary right
            songs.delete()
            p.delete()
        except Playlist.DoesNotExist:
            raise HttpResponse(status=400)
        return HttpResponse()
    else:
        return render(request,'index.html')

@login_required
def delete_song(request, playlist_slug, pk):
    """
    Delete a song by PK from playlist
    when DELETE request is sent to /library/<pl>/<pk>/
    """
    if (request.method == 'DELETE'):
        try:
            p = Playlist.objects.get(slug=playlist_slug,
                                     owner=request.user)
            s = Sound.objects.get(pk=pk)
            s.delete()
            # check if this song is in other playlists
            # if not, delete it too
            return HttpResponse('Congrats you found this page')
        except Playlist.DoesNotExist:
            raise Http404('Playlist does not exist')
    else:
        raise Http404
            

@login_required
def playlists_json(request):
    ps = Playlist.objects.filter(owner=request.user).values('name')
    return HttpResponse(json.dumps(list(ps)),
                        content_type='application/json')
    
# TODO maybe move this fn to another file?
@login_required
def list_of_playlists(request):
    """
    Return a list of all playlists owned by user
    when an HTTP request is made to /playlists/all
    """
    if (request.method == 'POST'):
        try:
            name = request.POST['name']
            # TODO handle invalid names eg already own this name
            p = Playlist(name=name, owner=request.user)
            p.save()
            return HttpResponse()
            # django.db.utils.IntegrityError
        except IntegrityError:
            # TODO unsure if we want this behaviour
            raise Http404('Playlist already exists')
    else:
        playlists = Playlist.objects.filter(owner=request.user)
        return render(request,'playlist_select.html', {'playlists': playlists})
