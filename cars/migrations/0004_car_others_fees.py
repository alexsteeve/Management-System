# Generated by Django 4.1.7 on 2023-03-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_late_payment_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='others_fees',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
