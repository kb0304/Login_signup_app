from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import login
import os


def ag53_home_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/ag53/profile')
    else:
        return HttpResponseRedirect('/ag53/login')


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
@login_required

def profile_view(request):
    u = request.user
    context = {'user':u, 'base_path': os.path.join(BASE_DIR,''),'pp':u.profile.profile_pic,'cp':u.profile.cover_pic}
    return render(request, 'ag53/profile.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/ag53/')

def change_password(request):
    if POST:
        p = request.POST['new_password']
        request.user.set_password(p)
