# Generated by Django 3.1.4 on 2021-01-03 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210103_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='order',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='order',
            name='width_field',
        ),
    ]