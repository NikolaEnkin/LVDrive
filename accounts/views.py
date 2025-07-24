from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import AppUserCreationForm


class RegisterView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('#')
    # Uses signal to create the profile