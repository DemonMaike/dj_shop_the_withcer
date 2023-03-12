#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """ homepage"""

    context = {
        'title': 'homepage'
    }
    return render(request, 'base.html', context)


def about(request):
    """ page about us"""

    return HttpResponse('О нас')


def category(request):
    """ all categoryes """
    return HttpResponse('Все категории')


def allproducts(request):
    """all products"""
    return HttpResponse('Все товары')
