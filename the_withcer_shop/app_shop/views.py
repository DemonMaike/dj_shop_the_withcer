from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from app_shop.models import *
from app_cart.forms import CartAddProductForm
from app_cart.cart import Cart
from django.views.generic import *
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CreateUserForm


class ShopHome(TemplateView):
    template_name = 'home.html'
    extra_context = {'title': 'homepage'}
        
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['cart'] = Cart(request)
        return self.render_to_response(context)
    
class ShopAbout(TemplateView):
    template_name = 'about.html'
    extra_context = {'title': 'about'}
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['cart'] = Cart(request)
        return self.render_to_response(context)
    
class ShopACategories(ListView):
    model = Category
    template_name = 'category.html'
    extra_context = {'title': 'category'}
    context_object_name = 'category'
    

class ShowCategory(ListView):
    model = Product
    template_name = 'currentcategory.html'
    pk_url_kwarg = 'cur_category'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['cur_category'])
    
class ShopProducts(ListView):
    model = Product
    template_name = 'allproducts.html'
    context_object_name = 'product'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class ShowProduct(DetailView):
    model = Product
    pk_url_kwarg = 'cur_product'
    template_name = 'currentproduct.html'
    context_object_name = 'product'
    extra_context = {'title': 'All products'} # Problem, don't show title on the page
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_for_cart'] = CartAddProductForm()
        context['title'] = 'All Products'
        return context

class LoginUser(LoginView):
    redirect_authenticated_user = True
    template_name = 'authentication.html'
    
    def get_success_url(self):
        return reverse_lazy('shop_app:home')
        
class RgisterUser(FormView):
    form_class = CreateUserForm
    template_name = 'register.html'
    success_url = 'shop_app:home'
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'])
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return reverse(self.success_url)
    
class LogoutUser(LogoutView):
    http_method_names = ['post']
    template_name = 'home.html'
    extra_context = {'comment': 'You are logout', 'title': 'homepage'}