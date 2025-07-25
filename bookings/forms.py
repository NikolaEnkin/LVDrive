from django import forms

from bookings.models import Booking


class BaseBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_datetime', 'end_datetime']

        widgets = {
            'start_datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
            'end_datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }

        labels = {
            'start_datetime': 'Pick‑up',
            'end_datetime': 'Drop‑off',
        }

class CreateBookingForm(BaseBookingForm):
    ...

class EditBookingForm(BaseBookingForm):
    ...

