# Generated by Django 4.1.7 on 2023-03-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_fixed_fee_alter_car_late_payment_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dismantle',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='transport',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='weight',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
