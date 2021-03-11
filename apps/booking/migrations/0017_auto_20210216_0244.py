# Generated by Django 3.1.2 on 2021-02-16 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_rooms_featuresid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='FeaturesId',
        ),
        migrations.AddField(
            model_name='rooms',
            name='FeaturesId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.features'),
        ),
    ]