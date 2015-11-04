from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	template = loader.get_template('registration/index.html')
	return HttpRsponse(template)

# Create your views here.
