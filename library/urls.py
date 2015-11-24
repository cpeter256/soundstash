from django.conf.urls import url

from .views import *
import library_json.views

urlpatterns = [
    url(r'(?P<playlist>[\w-]+)/add/$', add_song),
    url(r'^add/$', add_song),

    url(r'^library_json/$', library_json.views.libraryView),
    url(r'^(?P<playlist_name>[\w-]+)/library_json/$', library_json.views.libraryView),

    url(r'^$|^[\w-]+/$', playlist),
]