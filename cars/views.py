from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.generic.detail import View
from django.utils import timezone
from .models import Car, Part, Prices
from django.core.paginator import Paginator
from django.http import HttpResponse
import requests
from dotenv import dotenv_values
import os
import pprint
import json
import re

class PriceForm(ModelForm):
    class Meta:
        model = Prices
        fields = ['type', 'year_init', 'year_final', 'make', 'model', 'engine', 'driver_type', 'price', 'buyer']

def price_create(request):
    form = PriceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prices')
    return render(request, 'price_form.html', {'form': form})

def price_list(request):
    prices = Prices.objects.all()
    print(prices.values())
    return render(request, 'price_list.html', {'prices': prices})

def price_update(request, id):
    price = get_object_or_404(Prices, id=id)
    form = PriceForm(request.POST or None, instance=price)
    if form.is_valid():
        form.save()
        return redirect('prices')
    return render(request, 'price_form.html', {'form': form})

def price_delete(request, id):
    price = get_object_or_404(Prices, id=id)
    if request.method == 'POST':
        price.delete()
        return redirect('prices')
    return render(request, 'price_confirm_delete.html', {'price': price})

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['date', 'year', 'make', 'model', 'LOT', 'VIN', 'site', 'status', 'bid', 'buyer_fee', 'fixed_fee', 'storage_fee', 'late_payment_fee', 'others_fees', 'transport', 'dismantle', 'weight', 'picture']

def car_list(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'cars': cars}

    return render(request, 'car_list.html', {'page_obj': page_obj})

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

class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['VIN', 'status', 'type', 'max_value', 'value_paid']

def part_list(request):
    parts = Part.objects.all()
    return render(request, 'part_list.html', {'parts': parts})

def part_create(request):
    form = PartForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parts')
    return render(request, 'part_form.html', {'form': form})

def part_update(request, id):
    part = get_object_or_404(Part, id=id)
    form = PartForm(request.POST or None, instance=part)
    if form.is_valid():
        form.save()
        return redirect('parts')
    return render(request, 'part_form.html', {'form': form})

def part_delete(request, id):
    part = get_object_or_404(Part, id=id)
    if request.method == 'POST':
        part.delete()
        return redirect('parts')
    return render(request, 'part_confirm_delete.html', {'part': part})

class CarDetailView(View):
    def get(self, request, *args, **kwargs):
        # car = get_object_or_404(Car, pk=kwargs['pk'])
        car = get_object_or_404(Car, pk=kwargs['VIN'])
        context = {'car': car}
        context['part'] = Part.objects.filter(VIN=self.kwargs['VIN'])
        return render(request, 'car_detail.html', context)

def vins(request):
    vinReceived = request.GET.get("vinField")
    response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/' + vinReceived + '?format=json')
    vins = response.json()
    
    prices = Prices.objects.all()
    prices = list(prices)
    pricesMatched = []
    expected_price = copyMatches(prices , vins, pricesMatched)

    context = {'vins': vins}
    context['prices'] = pricesMatched
    context['expected_price'] = expected_price

    return render(request, "vins.html", context)
    pass

def copyMatches(prices , vins, pricesMatched):
    expected_price = 590
    yearVin = int(vins["Results"][10]["Value"])
    make = (vins["Results"][7]["Value"]).upper()
    model = (vins["Results"][9]["Value"]).upper()
    liter = (vins["Results"][73]["Value"])
    driverType = (vins["Results"][51]["Value"])
    previous_type = ""
    if  str(prices[9].driver_type.upper()) in str(driverType):
        print("yes")
    else:
        print("no")
    for i in range(len(prices)):
        copy = True
        if not(prices[i].year_init <= yearVin and prices[i].year_final >= yearVin):
            copy = False
        if (not(str(prices[i].make.upper()) in str(make)) and prices[i].make != "ANY"):
            copy = False
        if (not(str(prices[i].model.upper()) in str(model)) and prices[i].model != "ANY"):
            copy = False
        if (prices[i].engine != liter and prices[i].engine != "ANY"):
            copy = False
        if (not(str(prices[i].driver_type.upper()) in str(driverType)) and prices[i].driver_type != "ANY"):
            copy = False
        if (copy and previous_type != prices[i].type):
            pricesMatched.append(prices[i])
            expected_price = expected_price + prices[i].price
            previous_type = prices[i].type
    return expected_price