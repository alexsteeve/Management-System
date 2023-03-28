import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CarFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    make = CharFilter(field_name="make", lookup_expr='icontains')
    model = CharFilter(field_name="model", lookup_expr='icontains')
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['site', 'buyer_fee', 'fixed_fee', 'storage_fee', 'late_payment_fee', 'others_fees', 'transport', 'dismantle', 'weight', 'picture', 'bid', 'date', 'status']