from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView
from cars.models import Car


class HomePageView(TemplateView):
    def get_template_names(self):
        if not self.request.user.is_authenticated:
            return ['home/home-page-not-authenticated.html']
        else:
            return ['cars/cars-dashboard.html']