from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, FormView, DeleteView
from accounts.forms import AppUserCreationForm, EditProfileForm
from accounts.models import Profile


class RegisterView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    # Uses signal to create the profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'registration/profile-details-page.html'


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'registration/profile-edit-page.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'registration/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        user = self.object.user
        profile.delete()
        user.delete()
        return redirect(self.success_url)
