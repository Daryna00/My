# Generated by Django 3.1.3 on 2020-12-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0024_auto_20201208_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
