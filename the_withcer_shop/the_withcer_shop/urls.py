from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_shop.urls')),
    re_path(r'^cart/', include('app_cart.urls', namespace='cart_app')),
]
