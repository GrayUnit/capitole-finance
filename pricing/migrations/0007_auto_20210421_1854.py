# Generated by Django 3.2 on 2021-04-21 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0006_auto_20210421_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicule',
            old_name='km',
            new_name='km_initial',
        ),
        migrations.AlterField(
            model_name='pricinginfo',
            name='date_modification',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 18, 54, 23, 585331, tzinfo=utc)),
        ),
    ]
