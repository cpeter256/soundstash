import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import userForm

def register(request):
	print request
	if request.method == "POST":
		form = userForm(request.POST)
		first_name = request.POST.get('First_name')
		last_name  = request.POST.get('Last_name')
		usr_name   = request.POST.get('username')
		email      = request.POST.get('email')
		password   = request.POST.get('password')

		new_user  = User.objects.create_user(usr_name, email, password)
        	new_user.first_name = first_name
		new_user.last_name  = last_name
		new_user.save()

		#this is prob bad code
		user = auth.authenticate(username=usr_name, password=password)
		auth.login(request, user)
		return HttpResponseRedirect('/')
	else:
		form = userForm()
		
	return render(request, 'registration.html', {'form': form})

