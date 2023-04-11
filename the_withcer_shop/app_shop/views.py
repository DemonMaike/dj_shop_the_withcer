from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from app_shop.models import *
from app_cart.forms import CartAddProductForm
from app_cart.cart import Cart

# --- Website ---
def home(request):
    """ homepage"""
    cart = Cart(request)
    context = {
        'title': 'homepage',
        'cart': cart,
    }
    return render(request, 'home.html', context)


def about(request):
    """ page about us"""
    cart = Cart(request)
    context = {
        'title': 'about',
        'cart': cart,
    }
    return render(request, 'about.html', context)


def category(request):
    """ all categoryes """
    cart = Cart(request)
    context = {
        'title': 'category',
        'cart': cart,
    }
    return render(request, 'category.html', context)

def currentcategory(request, cur_category):
    """View for select category"""
    cart = Cart(request)
    cat_products = Product.objects.filter(category=cur_category)
    context = {
        'products': cat_products,
        'cart': cart,
    }
    return render(request, 'currentcategory.html', context)

def allproducts(request):
    """all products"""
    cart = Cart(request)
    context = {
        'title': 'allproducts',
        'cart': cart,
    }
    return render(request, 'allproducts.html', context)

def currentproduct(request, cur_product):
    """View for select product"""
    cart = Cart(request)
    
    context = {
        'title': f'Current product {cur_product}',
        'form_for_cart': CartAddProductForm(),
        'id': cur_product,
        'cart': cart,
    }
    return render(request,'currentproduct.html',context)


# --- Auth/Sign Up/Logout ---
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
            return redirect('shop_app:home')

    

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
    return redirect('shop_app:home')