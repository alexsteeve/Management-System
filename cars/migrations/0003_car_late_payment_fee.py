# Generated by Django 4.1.7 on 2023-03-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_storage_fee_alter_car_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='late_payment_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
