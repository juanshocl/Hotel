# Generated by Django 3.1.2 on 2021-03-18 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0025_auto_20210317_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='DateCheckIn',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 23, 56, 23, 106826), verbose_name='Check In'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateCheckOut',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 23, 56, 23, 106856), verbose_name='CheckOut'),
        ),
    ]
