from django.core.management.base import BaseCommand
from app_shop.models import Product, Category
import random


class Command(BaseCommand):
    '''
    Creaeting testing database
    '''
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        products = []
        categories = []

        for i in range(1, 4):
            categories.append(
                Category(
                    name=f'Category_{i}'
                    )
            )
        
        Category.objects.bulk_create(categories)
        
        for i in range(0, 31):
            products.append(
            Product(
                name=f'Porduct_{i}',
                description=f'Description for Product_{i}',
                price=random.randint(1000,2000),
                category=Category.objects.get(name='Category_1')
                )
            )
        
        
        Product.objects.bulk_create(products)

        print('Created data of database')
        
