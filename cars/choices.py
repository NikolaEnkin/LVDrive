from django.db import models

class CarBodyTypeChoices(models.TextChoices):
    SEDAN = 'sedan', 'Sedan'
    SUV = 'suv', 'SUV'
    HATCHBACK = 'hatchback', 'Hatchback'
    COUPE = 'coupe', 'Coupe'
    CONVERTIBLE = 'convertible', 'Convertible'
    WAGON = 'wagon', 'Wagon'

class CarFuelTypeChoices(models.TextChoices):
    GASOLINE = 'gas', 'Gasoline'
    DIESEL   = 'diesel',   'Diesel'
    ELECTRIC = 'el', 'Electric'
    HYBRID   = 'hyb',   'Hybrid'
    OTHER = 'other', 'Other'
