# Generated by Django 3.1.3 on 2020-12-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0015_merchandise_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='height_field',
            field=models.SmallIntegerField(null=True),
        ),
    ]
