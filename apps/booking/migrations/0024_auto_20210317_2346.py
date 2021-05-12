# Generated by Django 3.1.2 on 2021-03-18 02:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_auto_20210317_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Is_Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateCheckIn',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 23, 46, 34, 295251), verbose_name='Check In'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateCheckOut',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 23, 46, 34, 295280), verbose_name='CheckOut'),
        ),
    ]