from django.contrib import admin
from cars.models import Car, CarImage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model_name', 'price_per_hour']
    list_filter = ['make', 'model_name', 'price_per_hour']
    ordering = ['price_per_hour']

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'car_model', 'uploaded_at']
    ordering = ['-uploaded_at']

    def car_make(self, obj):
        return obj.car.make

    def car_model(self, obj):
        return obj.car.model_name