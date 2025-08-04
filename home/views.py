from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/home-page-not-authenticated.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('cars-dashboard')
        return super().dispatch(request, *args, **kwargs)

class AboutUsView(TemplateView):
    template_name = 'home/about-us-page.html'

class ContactUsView(TemplateView):
    template_name = 'home/contact-us-page.html'