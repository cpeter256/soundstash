from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from .forms import AddSongForm
from .models import Sound

def index(request):
    """
    Display main library page with songs
    """
    return render_to_response('index.html')

def add_song(request):
    """
    Add new song to music db by processing POST
    """
    if (request.method == 'POST'):
        form = AddSongForm(request.POST)
        if form.is_valid():
            uri = form.cleaned_data['uri']
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            Sound(uri, title, artist).save() # TODO can this fail
            return HttpResponseRedirect('/') # TODO tell user that it worked!!
    else:
        form = AddSongForm()
    return render(request, 'add.html', {
        'form': form,
    })

