# Generated by Django 2.0.6 on 2018-07-20 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_auto_20180720_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dcat',
            name='drink_item',
        ),
        migrations.AddField(
            model_name='ditem',
            name='drink_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drinks.Dcat'),
        ),
    ]
