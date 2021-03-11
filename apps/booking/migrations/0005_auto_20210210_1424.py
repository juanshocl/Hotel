# Generated by Django 3.1.2 on 2021-02-10 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210210_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Mount',
            field=models.IntegerField(default=None, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateCheckIn',
            field=models.DateField(default=None, verbose_name='Fecha CheckIn'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateCheckOut',
            field=models.DateField(default=None, verbose_name='Fecha CheckOut'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='TimeCheckIn',
            field=models.TimeField(default=None, verbose_name='Hora CheckIn'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='TimeCheckOut',
            field=models.TimeField(default=None, verbose_name='Hora CheckOut'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CategoryDescription',
            field=models.CharField(default=None, max_length=50, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='features',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='PaymentMethodDescription',
            field=models.CharField(default=None, max_length=50, verbose_name='Metodo de pago'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='roomstype',
            name='Id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]