from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def home(request):
    """ homepage"""

    context = {
        'title': 'homepage',
    }
    return render(request, 'home.html', context)


def about(request):
    """ page about us"""
    context = {
        'title': 'about'
    }
    return render(request, 'about.html', context)


def category(request):
    """ all categoryes """
    context = {
        'title': 'category'
    }
    return render(request, 'category.html', context)


def allproducts(request):
    """all products"""
    context = {
        'title': 'allproducts'
    }
    return render(request, 'allproducts.html', context)

def authentication(request):
    """ Auth form """
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm(),
        }
        return render(request, 'authentication.html', context)
    else:
        user = authenticate(request=request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            context = {
            'form': AuthenticationForm(),
            'error': 'Login or password is not corrected. Try again.'
            }
            return render(request, 'authentication.html', context)
        else:
            login(request, user)
            return redirect('home')

    

def register(request):
    """register from"""
    if request.method == "GET":
        context = {
            'form': UserCreationForm(),
        }
        return render(request, 'register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                 password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'You alredy register, please, login.',
                    }
                return render(request, "register.html", context)
        else:
            context = {
            'form': UserCreationForm(),
            'error': 'Your passwords is not same, please, try again.'
            }
            return render(request, "register.html", context)


def logout_user(request):
    """method for logout a user"""
    if request.method == "POST":
        logout(request)
    return redirect('home')