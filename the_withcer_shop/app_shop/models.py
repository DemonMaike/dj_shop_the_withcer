from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
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
        verbose_name='Photo of products',
        blank=True
        )
    category = models.ForeignKey(
        'Category',
         on_delete=models.CASCADE,
         related_name='category'
        )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop_app:currentproduct', kwargs={'cur_product': self.pk})
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Category'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_app:currentcategory', kwargs={'cur_category': self.pk})
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Cart(models.Model):
    cart = models.ManyToManyField('Product', related_name='products')