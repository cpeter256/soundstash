from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from .forms import AddSongForm
from .models import Sound, Playlist

def index(request):
    return render_to_response('index.html')

def playlist(request):
    """
    Display "playlist" page with songs
    """
    return render_to_response('index.html')

def add_song(request, playlist='default'):
    """
    Add new song to music db by processing POST
    """
    if (request.method == 'POST'):
        form = AddSongForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            # TODO handle failures
            s = Sound(url=url, title=title, artist=artist)
            s.save()
            # TODO handle nonexistant playlist
            p = Playlist.objects.get(owner__username='thelatecomers',
                                     slug=playlist)
            p.sound.add(s)
            p.save()
            return HttpResponseRedirect('..') # TODO tell user that it worked!!
    else:
        form = AddSongForm()

    return render(request, 'add.html', {
        'form': form,
    })
