from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'add/$|add.html', add_song),
]
