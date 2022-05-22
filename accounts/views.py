from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt


def home(request):

    return render(request, 'accounts/index.html')


@csrf_exempt
def signup(request):

    if request.method == 'GET':
        return render(request, 'accounts/signup.html', 
        {'form':UserCreateForm})

    if request.method == 'POST' and request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(request.POST['username'],
            password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('signin')
        except IntegrityError:
            return render(request, 'accounts/signup.html',
            {'form':UserCreateForm, 'error':'Username already taken. Choose new username. '})
    
    return render(request, 'accounts/signup.html',
    {'form':UserCreateForm, 'error':'Passwords do not match'})


def signin(request):
    return render(request, 'accounts/signin.html')


def signout(request):
    pass