# Generated by Django 3.1.2 on 2020-12-27 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InstanceProduct',
            new_name='StockLog',
        ),
    ]
