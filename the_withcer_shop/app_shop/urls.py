from django.urls import path
from . import views
from .views import ShopHome, ShopAbout, ShopACategories,\
    ShowCategory, ShopProducts, ShowProduct, LoginUser, LogoutUser, RgisterUser

app_name = 'shop_app'

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about', ShopAbout.as_view(), name='about'),
    path('category', ShopACategories.as_view(), name='category'),
    path('category/<int:cur_category>', ShowCategory.as_view(), name='currentcategory'),
    path('allproducts', ShopProducts.as_view(), name='allproducts'),
    path('allproducts/<int:cur_product>', ShowProduct.as_view(), name='currentproduct'),
    path('authentication', LoginUser.as_view(), name='authentication'),
    path('register', RgisterUser.as_view(), name='register'),
    path('logout', LogoutUser.as_view(), name='logoutuser'),
    
]
