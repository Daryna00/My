# Generated by Django 3.1.4 on 2021-01-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210103_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]