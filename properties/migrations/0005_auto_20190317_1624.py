# Generated by Django 2.1.7 on 2019-03-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20190317_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default=None, upload_to='properties/static/uploads/'),
        ),
    ]