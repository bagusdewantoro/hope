# Generated by Django 3.1.2 on 2020-12-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0013_auto_20201231_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
