from django.db import models

class BookingStatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    ACTIVE = 'ACTIVE', 'Active'
    CANCELLED = 'CANCELLED', 'Cancelled'