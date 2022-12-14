from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from music_services.web.forms import RecommendationCreateForm, ServiceCreateForm, ServiceEditForm, ServiceDeleteForm
from music_services.web.models import Service, Review


class ReviewCreateView(CreateView):
    template_name = 'review/review-create.html'
    model = Review
    fields = ['rating', 'description']


class ReviewDeleteView(DeleteView):
    template_name = 'review/review-delete.html'
    model = Review
    success_url = reverse_lazy('success')  # Same as Service Deletion


def index(request):
    context = {
    }

    return render(
        request,
        'index.html',
        context,
    )


def about(request):
    return render(
        request,
        'about/about.html',
    )


def catalogue(request):
    context = {
        'services': Service.objects.all()
    }

    return render(
        request,
        'catalogue/catalogue.html',
        context
    )


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
        'service/service-create.html',
        context
    )


def service_details(request, pk):
    service = Service.objects.filter(pk=pk).get()

    context = {
        'service': service,
    }

    return render(
        request,
        'service/service-details.html',
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
        'service/service-edit.html',
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
        'service/service-delete.html',
        context
    )


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
        'about/recommendation.html',
        context
    )
