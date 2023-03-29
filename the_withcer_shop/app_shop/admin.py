from django.contrib import admin
from .models import Product, Category, Card, Card_Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    fields = [('name', 'price'), 'description',
     'photo', 'category']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Card)
admin.site.register(Card_Product)
