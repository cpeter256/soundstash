from django.conf.urls import url

from .views import *
import library_json.views

urlpatterns = [
#    url(r'$', library_json.views.libraryView)
    url(r'add/$|add.html', add_song),
    url(r'^(?P<playlist_name>[\w-]+)/library_json/$', library_json.views.libraryView),
    url(r'^[\w-]+/$', playlist),
]
