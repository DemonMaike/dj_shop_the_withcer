# Generated by Django 4.1.7 on 2023-04-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0002_alter_product_category_alter_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ManyToManyField(related_name='products', to='app_shop.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='card_product',
            name='id_card',
        ),
        migrations.RemoveField(
            model_name='card_product',
            name='id_product',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Card_Product',
        ),
    ]