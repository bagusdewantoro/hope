# Generated by Django 3.1.2 on 2020-12-31 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0011_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stocklog',
            options={'ordering': ['production_date', 'product', 'quantity', 'sold'], 'verbose_name': 'Stock Log', 'verbose_name_plural': 'Stock Log'},
        ),
        migrations.RemoveField(
            model_name='stocklog',
            name='price',
        ),
    ]