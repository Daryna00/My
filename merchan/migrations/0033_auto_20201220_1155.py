# Generated by Django 3.1.4 on 2020-12-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0032_auto_20201209_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]