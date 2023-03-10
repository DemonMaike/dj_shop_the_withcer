from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('allproducts', views.allproducts, name='allproducts'),
]
