# Generated by Django 3.1.4 on 2021-01-03 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(default='', upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'zip', 'rar'])]),
        ),
    ]
