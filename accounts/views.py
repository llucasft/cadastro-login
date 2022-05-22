from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt


def home(request):

    return render(request, 'accounts/index.html')


@csrf_exempt
def logoutaccount(request):
    logout(request)
    return redirect('home')
    

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
            return redirect('home')
        except IntegrityError:
            return render(request, 'accounts/signup.html',
            {'form':UserCreateForm, 'error':'Username already taken. Choose new username. '})
    
    return render(request, 'accounts/signup.html',
    {'form':UserCreateForm, 'error':'Passwords do not match'})


def signin(request):

    if request.method == 'GET':
        return render(request, 'accounts/signin.html', {'form':AuthenticationForm})

    else:
        user = authenticate(request, username=request.POST['username'], 
        password=request.POST['password'])
    if user is None:
        return render(request, 'accounts/signin.html',
        {'form':AuthenticationForm(),
        'error':'username and password do not match'})
    else:
        login(request,user)
        return redirect('home')
