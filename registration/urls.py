from django.conf.urls import url
from registration import views

from . import views

urlpatterns = [
	url(r'^$', registration.index, name='index'),
]
