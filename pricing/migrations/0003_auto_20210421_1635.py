# Generated by Django 3.2 on 2021-04-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_rename_car_vehicule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='searched_counter',
        ),
        migrations.AddField(
            model_name='vehicule',
            name='marque',
            field=models.CharField(default='marque', max_length=255),
        ),
        migrations.AddField(
            model_name='vehicule',
            name='modele',
            field=models.CharField(default='modele', max_length=255),
        ),
    ]
