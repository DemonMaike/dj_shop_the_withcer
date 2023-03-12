#from django.shortcuts import render
from django.shortcuts import render


def home(request):
    """ homepage"""

    context = {
        'title': 'homepage'
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
