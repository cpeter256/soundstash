"""soundstash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

import library.views
import registration.views
import user_session.views
from . import views

urlpatterns = [
    url(r'^library_json/', include('library_json.urls')),
    url(r'^login/$', user_session.views.login),
    url(r'^logout/$', user_session.views.logout),
    url(r'^playlists/all/$', library.views.list_of_playlists),
    url(r'^playlists/all/$', library.views.playlists_json),
    url(r'^$', RedirectView.as_view(url='library/default',permanent=True)),
    url(r'^library/', include('library.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/$', registration.views.register)
]
