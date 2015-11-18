from django.shortcuts import render
from django.http import HttpResponse
import json

json_data = '[{"title":"__TITLE__","url":"__URL__","artist":"__ARTIST__"},{"title":"__TITLE__","url":"__URL__","artist":"__ARTIST__"}]'

data = json.loads(json_data)

def libraryView(request):
	return HttpResponse(json.dumps(data), content_type='application/json')

# Create your views here.
