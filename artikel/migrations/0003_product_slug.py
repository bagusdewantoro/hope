# Generated by Django 3.1.2 on 2020-12-31 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0002_auto_20201229_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]