# Generated by Django 4.1.7 on 2023-03-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_buyer_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='weight',
            field=models.IntegerField(),
        ),
    ]