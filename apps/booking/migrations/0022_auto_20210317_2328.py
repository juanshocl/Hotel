# Generated by Django 3.1.2 on 2021-03-18 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0021_auto_20210314_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='RoomsId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.rooms', verbose_name='Cabaña reservada'),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=1),
        ),
    ]
