import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import userForm
from library.models import Playlist

def register(request):
	if request.method == "POST":
		#grab user data //potentially not safe
		first_name = request.POST.get('First_name')
		last_name  = request.POST.get('Last_name')
		usr_name   = request.POST.get('username')
		email      = request.POST.get('email')
		password   = request.POST.get('password')

		#create the user object
		new_user  = User.objects.create_user(usr_name, email, password)
        	new_user.first_name = first_name
		new_user.last_name  = last_name
		new_user.save()

		#instantiate a default playlist
		p = Playlist(name='default', owner=new_user)
		p.save()

		#this is prob bad code
		try:
			user = auth.authenticate(username=usr_name, password=password)
			auth.login(request, user)
			return HttpResponseRedirect('/')
		except IntegrityError:
			raise Http404('User already exists')
	else:
		form = userForm()
		
	return render(request, 'registration.html', {'form': form})

