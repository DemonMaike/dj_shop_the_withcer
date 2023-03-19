from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('allproducts', views.allproducts, name='allproducts'),
    path('authentication', views.authentication, name='authentication'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logoutuser'),
]
