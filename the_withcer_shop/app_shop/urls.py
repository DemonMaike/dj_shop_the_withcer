from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('category/<slug:cur_category>', views.currentcategory, name='currentcategory'),
    path('allproducts', views.allproducts, name='allproducts'),
    path('allproducts/<slug:cur_product>', views.currentproduct, name='currentproduct'),
    path('authentication', views.authentication, name='authentication'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logoutuser'),
    
]
