# Generated by Django 3.2.18 on 2023-06-26 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
