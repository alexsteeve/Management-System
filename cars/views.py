from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.generic.detail import View
from django.utils import timezone
# from .filters import CarFilter
from .models import Car, Part
from django.core.paginator import Paginator
from django.http import HttpResponse
import requests
from dotenv import dotenv_values
import os

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['date', 'year', 'make', 'model', 'LOT', 'VIN', 'site', 'status', 'bid', 'buyer_fee', 'fixed_fee', 'storage_fee', 'late_payment_fee', 'others_fees', 'transport', 'dismantle', 'weight', 'picture']

def car_list(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # myFilter = CarFilter(request.GET, queryset=cars)
    # cars = myFilter.qs

    # context = {'cars': cars, 'myFilter': myFilter}
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
    response = requests.get('https://auto.dev/api/vin/ZPBUA1ZL9KLA00848?apikey=ZrQEPSkKYWxleHN0ZWV2ZUBnbWFpbC5jb20=')
    vins = response.json()

    return render(request, "vins.html", {'vins': vins})
    pass