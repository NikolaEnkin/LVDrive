from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from bookings.forms import CreateBookingForm, EditBookingForm, DeleteBookingForm
from bookings.models import Booking
from cars.models import Car


class CreateBookingView(CreateView):
    model = Booking
    template_name = 'bookings/booking-create-page.html'
    form_class = CreateBookingForm

    def get_car(self):
        return get_object_or_404(Car, pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['car'] = self.get_car()
        return kwargs

    def form_valid(self, form):
        form.instance.car = self.get_car()
        form.instance.booker = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car-details', kwargs={'pk': self.kwargs['pk']})


class EditBookingView(UpdateView):
    model = Booking
    template_name = 'bookings/edit-booking-page.html'
    form_class = EditBookingForm


class DeleteBookingView(DeleteView):
    model = Booking
    template_name = 'bookings/delete-booking-page.html'
    form_class = DeleteBookingForm
    success_url = reverse_lazy('cars-dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        booking = self.model.objects.get(pk=pk)
        return booking.__dict__

