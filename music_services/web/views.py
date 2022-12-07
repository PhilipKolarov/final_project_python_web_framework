from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from music_services.web.models import Profile, Service, Review


class ProfileCreateView(CreateView):
    model = Profile
    fields = ['username', 'email', 'password', 'first_name', 'last_name']


class ProfileEditView(UpdateView):
    model = Profile
    fields = '__all__'


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('success') # This is an HTML to which we will be redirected upon successful deletion


class ServiceCreateView(CreateView):
    model = Service
    fields = ['type', 'description', 'image_url', 'price']


class ServiceEditView(UpdateView):
    model = Service
    fields = '__all__'


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('success') # Same as Profile Deletion


class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'description']


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('success') # Same as Profile/Service Deletion
