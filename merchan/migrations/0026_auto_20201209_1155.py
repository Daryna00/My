# Generated by Django 3.1.3 on 2020-12-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0025_auto_20201208_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandise',
            old_name='height_field',
            new_name='height_field1',
        ),
        migrations.RenameField(
            model_name='merchandise',
            old_name='width_field',
            new_name='height_field2',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='width_field1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='width_field2',
            field=models.IntegerField(default=0),
        ),
    ]