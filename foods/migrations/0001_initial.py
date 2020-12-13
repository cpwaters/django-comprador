# Generated by Django 2.0.6 on 2018-07-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Food_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='None_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('body', models.TextField()),
            ],
        ),
    ]