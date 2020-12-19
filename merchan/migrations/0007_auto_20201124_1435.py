# Generated by Django 3.1.3 on 2020-11-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0006_merchandise_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merchandise',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='merchandise',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='img',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field'),
        ),
    ]
