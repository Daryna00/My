# Generated by Django 3.1.3 on 2020-12-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0027_auto_20201209_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='height_field1',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='height_field2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='width_field1',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='width_field2',
            field=models.IntegerField(default=1),
        ),
    ]