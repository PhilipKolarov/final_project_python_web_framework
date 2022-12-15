from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from music_services.web.forms import RecommendationCreateForm, ServiceCreateForm, ServiceEditForm, ServiceDeleteForm, \
    ReviewCreateForm
from music_services.web.models import Service, Review


UserModel = get_user_model()


class ReviewDeleteView(DeleteView):
    template_name = 'review/review-delete.html'
    model = Review
    success_url = reverse_lazy('success')  # Same as Service Deletion


def review_success(request):
    return render(
        request,
        'review/review-success.html',
    )


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
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect('details user', pk=request.user.pk)

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

    if request.method == 'GET':
        form = ReviewCreateForm(instance=service)
    else:
        form = ReviewCreateForm(request.POST, instance=service)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewed_service = service
            return redirect('service details', pk=service.pk)

    context = {
        'service': service,
        'form': form,
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
            return redirect('service details', pk=service.pk)

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
            return redirect('details user', pk=request.user.pk)

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
