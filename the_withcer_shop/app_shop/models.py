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
        return reverse('currentproduct', kwargs={'cur_product': self.pk})
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
        return reverse('currentcategory', kwargs={'cur_category': self.pk})
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Card(models.Model):
    id_user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
     )

    def __str__(self):
        return self.pk
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

    def __str__(self):
        return self.pk