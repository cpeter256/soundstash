from django.conf.urls import url

from .views import *
import library_json.views

urlpatterns = [

    url(r'^(?P<playlist>[\w-]+)/$', playlist_view),

    url(r'^(?P<playlist_name>[\w-]+)/library_json/$', library_json.views.libraryView),
]
