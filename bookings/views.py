from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from bookings.forms import CreateBookingForm
from bookings.models import Booking
from cars.models import Car


class CreateBookingView(CreateView):
    model = Booking
    template_name = 'bookings/booking-create-page.html'
    form_class = CreateBookingForm

    def get_car(self):
        return get_object_or_404(Car, pk=self.kwargs['car_pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance':Booking(car=self.get_car(), owner=self.request.user)})

        return kwargs
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)

        kwargs['car'] = self.get_car()

        return kwargs

    def get_success_url(self):
        return reverse('car-details', kwargs={'pk': self.kwargs['car_pk']})


