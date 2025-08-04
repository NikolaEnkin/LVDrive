from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from cars.forms import CreateCarForm, EditCarForm, SearchForm
from cars.models import Car, CarImage
from reviews.models import Review


class CarCatalogView(LoginRequiredMixin, ListView, PermissionRequiredMixin):
    model = Car
    paginate_by = 8
    template_name = 'cars/cars-dashboard.html'
    query_param = 'query'
    form_class = SearchForm
    context_object_name = 'cars'
    permission_required = 'cars.approve_car'

    def get_context_data(self, *, object_list = None, **kwargs):
        kwargs.update({
            "search_form": self.form_class(),
            "query":  self.request.GET.get(self.query_param, '')
        })

        return super().get_context_data(object_list=object_list, **kwargs)


    def get_queryset(self):
        queryset = self.model.objects.all()
        search_value = self.request.GET.get(self.query_param)

        if not self.has_permission():
            queryset = queryset.filter(approved=True)

        if search_value:
            queryset = queryset.filter(
                Q(make__icontains=search_value)
                |
                Q(model_name__icontains=search_value)
            )


        return queryset.order_by('-year')

def approve_car(request, pk):
    if request.method == 'POST':
        car = Car.objects.get(pk=pk)
        car.approved = True
        car.save()

        return redirect('cars-dashboard')

def deny_car(request, pk):
    if request.method == "POST":
        car = Car.objects.get(pk=pk)
        car.delete()

        return redirect('cars-dashboard')

class CarDetailsView(DetailView):
    model = Car
    template_name = 'cars/car-details-page.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        car = self.get_object()
        curr_time = timezone.now() + timedelta(hours=3)

        booking = car.car_bookings.filter(
            status='ACTIVE'
        ).first()

        reviews = Review.objects.filter(
            car=car,
        ).select_related(
            'reviewer'
        )

        can_review = self.request.user.is_authenticated and not reviews.filter(reviewer=self.request.user).exists()

        kwargs.update(
            {
                'bookings': booking,
                'now': curr_time,
                'car': car,
                'reviews': reviews,
                'can_review': can_review
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

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        car = self.get_object()

        add_images = car.car_images
        kwargs.update({"add_images": add_images})

        return kwargs


    def get_success_url(self):
        return reverse_lazy('car-details', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


class DeleteCarView(DeleteView):
    model = Car
    success_url = reverse_lazy('cars-dashboard')