from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response

def register(request):
	return render_to_response('registration.html')

# Create your views here.
