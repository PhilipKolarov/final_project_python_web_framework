from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from music_services.web.forms import RecommendationCreateForm, ServiceCreateForm, ServiceEditForm, ServiceDeleteForm
from music_services.web.models import Profile, Service, Review


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(
        request,
        'index.html',
        context
    )


class ProfileCreateView(CreateView):
    model = Profile
    fields = ['username', 'email', 'password', 'first_name', 'last_name']


class ProfileEditView(UpdateView):
    model = Profile
    fields = '__all__'


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('success') # This is an HTML to which we will be redirected upon successful deletion


def service_create(request):
    if request.method == 'GET':
        form = ServiceCreateForm()
    else:
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(
        request,
        'services-create.html',
        context
    )


def service_edit(request, pk):
    service = Service.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ServiceEditForm(instance=service)
    else:
        form = ServiceEditForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services details')

    context = {
        'form': form,
        'service': service,
    }

    return render(
        request,
        'services-edit.html',
        context
    )


def service_delete(request, pk):
    service = Service.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ServiceDeleteForm(instance=service)
    else:
        form = ServiceDeleteForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'service': service,
    }

    return render(
        request,
        'services-delete.html',
        context
    )


class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'description']


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('success') # Same as Profile/Service Deletion


# TODO Include accurate htmls, pages, and/or forms once written
def recommendation_create(request):
    if request.method == 'GET':
        form = RecommendationCreateForm()
    else:
        form = RecommendationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')

    context = {
        'form': form,
    }

    return render(
        request,
        '',
        context
    )


def about(request):
    context = {
    }

    return render(
        request,
        'about.html',
        context
    )
