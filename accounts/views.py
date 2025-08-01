from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accounts.forms import AppUserCreationForm
from accounts.models import Profile


class RegisterView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    # Uses signal to create the profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'registration/profile-details-page.html'

