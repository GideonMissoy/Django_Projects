from django.db import models

# Create your models here.
class Car(models.Model):
    price = models.CharField(max_length=255, null=False)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    car_model = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=255)
    interior_color = models.CharField(max_length=255)

  