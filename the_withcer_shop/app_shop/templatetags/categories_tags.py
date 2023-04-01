from django import template
from app_shop.models import Category

register = template.Library()

@register.simple_tag(name='all_categories')
def get_all_categories():
    return Category.objects.all()
    