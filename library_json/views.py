from django.shortcuts import render
from django.http import HttpResponse
import json

#filename = 'json_data2'
#json_file = open(filename, 'r')
#json_data = json_file.read()

json_data = '[{"title":"__TITLE__","url":"__URL__","artist":"__ARTIST__"},{"title":"__TITLE__","url":"__URL__","artist":"__ARTIST__"}]'

data = json.loads(json_data)

def libraryView(request):
	return HttpResponse(json.dumps(data), content_type='application/json')

# Create your views here.
