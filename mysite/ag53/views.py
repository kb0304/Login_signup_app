from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from ag53.forms import UserForm
from ag53.forms import ProfileForm
from django.template import RequestContext
import os



def ag53_home_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/ag53/profile')
    else:
        return HttpResponseRedirect('/ag53/login')


def signup(request):
    if request.method == 'POST':
        userform = UserForm(request.POST, prefix='user')
        profileform = ProfileForm(request.POST, request.FILES , prefix='profile')
        if userform.is_valid() * profileform.is_valid():
            user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponse('<h1>Sign up successfull. <a href="/ag53/login">Login here</a>.</h1>')
    else:
        userform = UserForm(prefix='user')
        profileform = ProfileForm(prefix='profile')
    return render_to_response('ag53/signup.html',dict(userform=userform,profileform=profileform),context_instance=RequestContext(request))



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
@login_required

def edit_profile(request):
    u = request.user
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES , prefix='profile')
        if profileform.is_valid():
            u.profile.delete()
            profile = profileform.save(commit=False)
            profile.user=u
            profile.save()
            return HttpResponseRedirect('/ag53/profile')
    else:
        profileform = ProfileForm(prefix='profile',initial={'name':u.profile.name,'enrollment_no':u.profile.enrollment_no,
                'about_me':u.profile.about_me,'age':u.profile.age,'branch':u.profile.branch,'gender':u.profile.gender})
    return render_to_response('ag53/edit_profile.html',dict(profileform=profileform),context_instance=RequestContext(request))

def cpsuccess(request):
    u = request.user
    context = {'user':u, 'base_path': os.path.join(BASE_DIR,''),'pp':u.profile.profile_pic,'cp':u.profile.cover_pic}
    return render(request, 'ag53/cpsuccess.html', context)


def profile_view(request):
    u = request.user
    context = {'user':u, 'base_path': os.path.join(BASE_DIR,''),'pp':u.profile.profile_pic,'cp':u.profile.cover_pic}
    return render(request, 'ag53/profile.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/ag53')

def change_password(request):
    if POST:
        p = request.POST['new_password']
        request.user.set_password(p)
