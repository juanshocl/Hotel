# Generated by Django 3.1.2 on 2021-01-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='test',
        ),
    ]
