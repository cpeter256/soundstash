from django.conf.urls import url

from .views import *
import library_json.views

urlpatterns = [
    url(r'add/$|add.html', add_song),
    url(r'default/$', index),
    url(r'default/library_json', library_json.views.libraryView),
]
