# Generated by Django 3.1.2 on 2021-01-01 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0016_awareness'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awareness',
            name='description',
        ),
    ]