from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

@login_required
def profile_view(request):
    u = request.user
    context = {'user':u,}
    return render(request, 'ag53/profile.html', context)
