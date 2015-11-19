from django.conf.urls import url

#import library_json.views
from library_json.views import libraryView

urlpatterns = [ url(r'^$', libraryView, name='libraryView'), ]
