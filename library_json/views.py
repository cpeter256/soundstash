from django.shortcuts import render
from django.http import HttpResponse
import json

from library.models import Sound

def libraryView(request):
    # Hopefully this is an efficient query. Requires further investigation.
    data = Sound.objects.filter(playlist__name='default',
                                playlist__owner__username='thelatecomers').values('artist','title','url')
    return HttpResponse(json.dumps(list(data)), content_type='application/json')
