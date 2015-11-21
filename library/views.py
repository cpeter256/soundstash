from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

from .forms import AddSongForm
from .models import Sound, Playlist

@login_required
def index(request):
    """
    Display main library page with songs
    """
    return render_to_response('index.html')

@login_required
def add_song(request):
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
            p = Playlist.objects.get(owner__username='thelatecomers',
                                     name='default')
            p.sound.add(s)
            p.save()
            return HttpResponseRedirect('/') # TODO tell user that it worked!!
    else:
        form = AddSongForm()
    return render(request, 'add.html', {
        'form': form,
    })

