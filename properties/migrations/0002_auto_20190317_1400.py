# Generated by Django 2.1.7 on 2019-03-17 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Status'),
        ),
    ]