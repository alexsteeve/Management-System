from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['date', 'year', 'make', 'model', 'LOT', 'VIN', 'site', 'status', 'bid', 'buyer_fee', 'fixed_fee', 'storage_fee', 'late_payment_fee', 'others_fees', 'transport', 'dismantle', 'weight']

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_create(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'car_form.html', {'form': form})

def car_update(request, id):
    car = get_object_or_404(Car, id=id)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'car_form.html', {'form': form})

def car_delete(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('index')
    return render(request, 'car_confirm_delete.html', {'car': car})
