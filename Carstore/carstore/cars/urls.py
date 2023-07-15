from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list, name='car_list'),
    path('create', views.create_car, name='create_car'),
]
