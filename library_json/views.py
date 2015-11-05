from django.shortcuts import render
from django.http import HttpResponse
import json

json_data = '[{"title":"foo","url":"blah.bar"},{"title":"baz","url":"quux.quuux"}]'

data = json.loads(json_data)

def libraryView(request):
	return HttpResponse(json.dumps(data), content_type='application/json')

# Create your views here.
