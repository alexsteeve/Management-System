from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.generic.detail import View
from django.utils import timezone
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponse
import requests
from dotenv import dotenv_values
import os
import pprint
import json
import re
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class PriceForm(ModelForm):
    class Meta:
        model = Prices
        fields = ['type', 'year_init', 'year_final', 'make', 'model', 'engine', 'driver_type', 'price', 'buyer']


@login_required(login_url='login')
def price_create(request):
    form = PriceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prices')
    return render(request, 'price_form.html', {'form': form})


@login_required(login_url='login')
def price_list(request):
    prices = Prices.objects.all()
    print(prices.values())
    return render(request, 'price_list.html', {'prices': prices})


@login_required(login_url='login')
def price_update(request, id):
    price = get_object_or_404(Prices, id=id)
    form = PriceForm(request.POST or None, instance=price)
    if form.is_valid():
        form.save()
        return redirect('prices')
    return render(request, 'price_form.html', {'form': form})


@login_required(login_url='login')
def price_delete(request, id):
    price = get_object_or_404(Prices, id=id)
    price.delete()
    return redirect('prices')


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['date', 'year', 'make', 'model', 'LOT', 'VIN', 'site', 'status', 'bid', 'buyer_fee', 'fixed_fee',
                  'storage_fee', 'late_payment_fee', 'others_fees', 'transport', 'dismantle', 'weight', 'picture']


@login_required(login_url='login')
def car_list(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'cars': cars}

    return render(request, 'car_list.html', {'page_obj': page_obj})


@login_required(login_url='login')
def car_create(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'car_form.html', {'form': form})


@login_required(login_url='login')
def car_update(request, id):
    car = get_object_or_404(Car, id=id)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'car_form.html', {'form': form})


@login_required(login_url='login')
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


@login_required(login_url='login')
def part_list(request):
    parts = Part.objects.all()
    return render(request, 'part_list.html', {'parts': parts})


@login_required(login_url='login')
def part_create(request):
    form = PartForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parts')
    return render(request, 'part_form.html', {'form': form})


@login_required(login_url='login')
def part_update(request, id):
    part = get_object_or_404(Part, id=id)
    form = PartForm(request.POST or None, instance=part)
    if form.is_valid():
        form.save()
        return redirect('parts')
    return render(request, 'part_form.html', {'form': form})


@login_required(login_url='login')
def part_delete(request, id):
    part = get_object_or_404(Part, id=id)
    part.delete()
    return redirect('parts')


class CarDetailView(View):
    def get(self, request, *args, **kwargs):
        # car = get_object_or_404(Car, pk=kwargs['pk'])
        car = get_object_or_404(Car, pk=kwargs['VIN'])
        context = {'car': car}
        context['part'] = Part.objects.filter(VIN=self.kwargs['VIN'])
        return render(request, 'car_detail.html', context)


@login_required(login_url='login')
def vins(request):
    vinReceived = str(request.GET.get("vinField"))
    response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/' + vinReceived + '?format=json')
    vins = response.json()

    prices = Prices.objects.all()
    prices = list(prices)
    pricesMatched = []
    context = {'vins': vins}
    if (vins["Results"][0]["Value"] != "N!NE"):
        expected_price = copyMatches(prices, vins, pricesMatched)
        context['expected_price'] = expected_price
        context['prices'] = pricesMatched

    return render(request, "vins.html", context)
    pass


def copyMatches(prices, vins, pricesMatched):
    expected_price = 590
    yearVin = int(vins["Results"][10]["Value"])
    make = (vins["Results"][7]["Value"]).upper()
    model = (vins["Results"][9]["Value"]).upper()
    liter = (vins["Results"][73]["Value"])
    driverType = (vins["Results"][51]["Value"])
    if (driverType == "4x2"):
        driverType = "4WD"
    turbo = (vins["Results"][87]["Value"])
    previous_type = ""
    for i in range(len(prices)):
        copy = True
        if not (prices[i].year_init <= yearVin and prices[i].year_final >= yearVin):
            copy = False
        if (not (str(prices[i].make.upper()) in str(make)) and prices[i].make != "ANY"):
            copy = False
        if (not (str(prices[i].model.upper()) in str(model)) and prices[i].model != "ANY"):
            copy = False
        if (not (str(liter) in str(prices[i].engine)) and prices[i].engine != "ANY"):
            copy = False
        if ((not (str(prices[i].driver_type.upper()) in str(driverType)) and prices[i].driver_type != "ANY") and (
                turbo != "Yes" and prices[i].driver_type != "TURBO")):
            copy = False
        if (copy and previous_type != prices[i].type):
            pricesMatched.append(prices[i])
            expected_price = expected_price + prices[i].price
            previous_type = prices[i].type
    return expected_price
