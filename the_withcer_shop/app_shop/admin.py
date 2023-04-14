from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    fields = [('name', 'price'), 'description',
     'photo', 'category']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

