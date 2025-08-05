from django.contrib import admin
from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'status']
    list_filter = ['created_at']
    ordering = ['-created_at']