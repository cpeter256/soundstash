from django import forms

class AddSongForm(forms.Form):
    url = forms.URLField(label='Link', max_length=100) # TODO max len?
    artist = forms.CharField(label='Artist')
    title = forms.CharField(label='Title')
