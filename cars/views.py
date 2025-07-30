from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from cars.forms import CreateCarForm, EditCarForm, SearchForm
from cars.models import Car, CarImage


class CarCatalogView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'cars/cars-dashboard.html'
    query_param = 'query'
    form_class = SearchForm
    context_object_name = 'cars'

    def get_context_data(self, *, object_list = None, **kwargs):
        kwargs.update({
            "search_form": self.form_class(),
            "query":  self.request.GET.get(self.query_param, '')
        })

        return super().get_context_data(object_list=object_list, **kwargs)


    def get_queryset(self):
        queryset = self.model.objects.all()
        search_value = self.request.GET.get(self.query_param)

        if search_value:
            queryset = queryset.filter(
                Q(make__icontains=search_value)
                |
                Q(model_name__icontains=search_value)
            )

        return queryset

class CarDetailsView(DetailView):
    model = Car
    template_name = 'cars/car-details-page.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        car = self.get_object()
        curr_time = timezone.now() + timedelta(hours=3)

        booking = car.car_bookings.filter(
            start_datetime__lte=curr_time,
            end_datetime__gte=curr_time,
            status='ACTIVE'
        ).first()

        kwargs.update(
            {
                'bookings': booking,
                'now': curr_time,
                'car': car
            }
        )

        return kwargs



class CreateCarView(CreateView):
    model = Car
    form_class = CreateCarForm
    success_url = reverse_lazy('cars-dashboard')
    template_name = 'cars/car-create-page.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response =  super().form_valid(form)

        images = self.request.FILES.getlist('images')

        for image in images:
            CarImage.objects.create(car=self.object, car_image=image)

        return response

class EditCarView(UpdateView):
    model = Car
    form_class = EditCarForm
    template_name = 'cars/car-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('car-details', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


class DeleteCarView(DeleteView):
    model = Car
    success_url = reverse_lazy('cars-dashboard')