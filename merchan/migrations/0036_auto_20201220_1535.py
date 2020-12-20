# Generated by Django 3.1.4 on 2020-12-20 13:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merchan', '0035_auto_20201220_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
