from django.contrib import admin
from cars.models import Car, CarImage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    ...