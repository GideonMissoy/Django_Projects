from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from .models import Car
from django.views.decorators.csrf import csrf_exempt
import json 
# Create your views here.
def cars_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        cars_json = serializers.serialize('json', cars)

        return JsonResponse(cars_json, safe=False)

@csrf_exempt
def create_car(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        car_created = Car.objects.create(
            price=data['price'],
            engine=data['engine'],
            brand=data['brand'],
            year=data['year'],
            car_model=data['car_model'],
            fuel_type=data['fuel_type'],
            interior_color=data['interior_color']
        )
        car_json = serializers.serialize('json', [car_created])
        return JsonResponse(car_json, safe=False)