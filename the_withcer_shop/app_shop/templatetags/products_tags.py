from django import template
from app_shop.models import * 
register = template.Library()

@register.simple_tag()
def get_product(pk=None):
    product = Product.objects.filter(pk=pk)
    return product

@register.simple_tag(name='all_products')
def get_all_products():
    return Product.objects.all()