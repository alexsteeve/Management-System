# Generated by Django 4.1.7 on 2023-03-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_buyer_fee_alter_car_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fixed_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='late_payment_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='others_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='storage_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
