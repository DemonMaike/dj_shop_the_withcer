from django.db import models

class Product(models.Model):
    """Model for products"""
    name = models.CharField(
        max_length=255, 
        verbose_name='Name of porduct'
        )
    description = models.TextField(
        verbose_name='Descripton'
        )
    price = models.IntegerField(
        verbose_name='Price'
        )
    photo = models.ImageField(
        upload_to='Product/%Y/%m/%d',
        verbose_name='Photo of products'
        )
    category = models.ForeignKey(
        'Category',
         on_delete=models.CASCADE
        )
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Category'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Card(models.Model):
    id_user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
     )

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

class Card_Product(models.Model):
    id_card = models.ForeignKey(
        'Card',
         on_delete=models.CASCADE
        )
    id_product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )

