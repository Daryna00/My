# Generated by Django 3.1.4 on 2020-12-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0033_auto_20201220_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]