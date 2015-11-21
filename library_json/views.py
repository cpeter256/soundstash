from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

from library.models import Sound

@login_required
def libraryView(request):
    # Hopefully this is an efficient query. Requires further investigation.
    data = Sound.objects.filter(playlist__name='default',
                                playlist__owner=request.user).values('artist','title','url')
    return HttpResponse(json.dumps(list(data)), content_type='application/json')
