from django.shortcuts import render
from django.http import HttpResponse
import json
import os

filename = 'json_data'
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
json_file = open(file_path, 'r')
json_data = json_file.read()

#json_data = '[{"title":"__TITLE__","url":"__URL__","artist":"__ARTIST__"},{"title":"__TITLE__","url":"__URL__","artist":"__ARTIST__"}]'

data = json.loads(json_data)

def libraryView(request):
	return HttpResponse(json.dumps(data), content_type='application/json')

# Create your views here.
