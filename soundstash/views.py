import django.contrib.auth as auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(request.GET.get('next'))
    else:
        # TODO Handle invalid login
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
