# Generated by Django 3.1.2 on 2020-12-31 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0014_product_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
