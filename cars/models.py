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
    picture = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.VIN

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
        ('brake_caliper_front_left', 'BRAKE CALIPER FRONT LEFT'),
        ('brake_caliper_front_right', 'BRAKE CALIPER FRONT RIGHT'),
        ('brake_caliper_rear_left', 'BRAKE CALIPER REAR LEFT'),
        ('brake_caliper_rear_right', 'BRAKE CALIPER REAR RIGHT'),
        ('catalyst', 'CATALYST'),
        ('climate_control_module', 'CLIMATE CONTROL MODULE'),
        ('drive_axle_front_left', 'DRIVE AXLE FRONT LEFT'),
        ('drive_axle_front_right', 'DRIVE AXLE FRONT RIGHT'),
        ('drive_axle_rear_left', 'DRIVE AXLE REAR LEFT'),
        ('drive_axle_rear_right', 'DRIVE AXLE REAR RIGHT'),
        ('electronic_throttle_body', 'ELECTRONIC THROTTLE BODY'),
        ('engine', 'ENGINE'),
        ('engine_control_module', 'ENGINE CONTROL MODULE'),
        ('eps_column', 'EPS COLUMN'),
        ('eps_rack', 'EPS RACK'),
        ('fan_from_radiator', 'FAN FROM RADIATOR'),
        ('footweel_module', 'FOOTWEEL MODULE'),
        ('inverter_hybrid_voltage_converter', 'INVERTER / HYBRID VOLTAGE CONVERTER'),
        ('manual_racks', 'MANUAL RACKS'),
        ('passenger_inflator', 'PASSENGER INFLATOR'),
        ('power_booster', 'POWER BOOSTER'),
        ('power_steering_pump', 'POWER STEERING PUMP'),
        ('rack_pinion_power', 'RACK & PINION POWER'),
        ('radiator', 'RADIATOR'),
        ('radio_audio', 'RADIO / AUDIO'),
        ('salvage', 'SALVAGE'),
        ('starter', 'STARTER'),
        ('tipm', 'TIPM'),
        ('tires', 'TIRES'),
        ('transfer_case', 'TRANSFER CASE'),
        ('transmission', 'TRANSMISSION'),
        ('transmission_control_module', 'TRANSMISSION CONTROL MODULE'),
        ('wheels', 'WHEELS'),
        ('wire', 'WIRE'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_PART_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    value_paid = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)

    def __str__(self):
       return self.type
