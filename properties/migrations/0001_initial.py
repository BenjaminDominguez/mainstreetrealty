# Generated by Django 2.1.7 on 2019-03-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=4000)),
                ('price', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=100)),
                ('year_built', models.CharField(max_length=100, verbose_name='year built')),
                ('sq_ft', models.IntegerField(verbose_name='square footage')),
                ('beds', models.IntegerField(verbose_name='beds')),
                ('full_baths', models.IntegerField(verbose_name='full baths')),
                ('half_baths', models.IntegerField(verbose_name='half baths')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
