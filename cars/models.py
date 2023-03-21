from django.db import models


class Car(models.Model):
    
    date = models.DateField()
    year = models.PositiveSmallIntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    LOT = models.CharField(max_length=100, blank=True)
    VIN = models.CharField(max_length=17, unique=True)
    site = models.CharField(max_length=100, blank=True)

    STATUS_CHOICES = [
        ('sold', 'Sold'),
        ('yard', 'In Yard'),
        ('remove_engine', 'Remove Engine'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    bid = models.DecimalField(max_digits=10, decimal_places=2)
    buyer_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fixed_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    storage_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    late_payment_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    others_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transport = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dismantle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.IntegerField()

    def __str__(self):
        return self.car

class Part(models.Model):
    VIN = models.ForeignKey(Car, default=1, on_delete=models.SET_DEFAULT)
    STATUS_PART_CHOICES = [
        ('in_the_car', 'IN THE CAR'),
        ('in_stock', 'IN STOCK'),
        ('sold', 'SOLD'),
    ]
    TYPE_CHOICES = [
        ('ac_compressor', 'A/C COMPRESSOR'),
        ('abs_module', 'ABS MODULE'),
        ('airbag', 'AIRBAG'),
        ('alternator', 'ALTERNATOR'),
        ('battery', 'BATTERY'),
        ('body_control_module', 'BODY CONTROL MODULE'),
        ('booster', 'BOOSTER'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_PART_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    value_paid = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)

    def __str__(self):
       return self.part
