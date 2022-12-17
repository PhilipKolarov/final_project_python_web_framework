from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView
from music_services.web.forms import RecommendationCreateForm, ServiceCreateForm, ServiceEditForm, ServiceDeleteForm, \
    ReviewCreateForm, ReviewEditForm, RecommendationEditForm, RecommendationDeleteForm, AnnouncementCreateForm, \
    AnnouncementEditForm, AnnouncementDeleteForm
from music_services.web.models import Service, Review, Recommendation, Announcement
from music_services.web.utils import calc_avg_review_score

UserModel = get_user_model()


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'review/review-delete.html'
    model = Review
    success_url = reverse_lazy('review success')


def index(request):
    announcements = Announcement.objects.all()

    context = {
        'announcements': announcements,
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


@login_required
def service_create(request):
    if request.method == 'GET':
        form = ServiceCreateForm()
    else:
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.date_added = timezone.now()
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
    reviews = Review.objects.filter(reviewed_service=service)

    avg_review_score = calc_avg_review_score(reviews)

    context = {
        'service': service,
        'reviews': reviews,
        'avg_review_score': avg_review_score,
    }

    return render(
        request,
        'service/service-details.html',
        context
    )


@login_required
def service_edit(request, pk):
    service = Service.objects.filter(pk=pk).get()

    if service.user == request.user:
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

    return render(request, '403-forbidden-access.html')


@login_required
def service_delete(request, pk):
    service = Service.objects.filter(pk=pk).get()

    if service.user == request.user:
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

    return render(request, '403-forbidden-access.html')


@login_required
def review_create(request, pk):
    service = Service.objects.filter(pk=pk).get()

    form = ReviewCreateForm(request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.reviewed_service = service
        review.date = timezone.now()
        review.save()
        return redirect('service details', pk=service.pk)

    context = {
        'form': form,
        'service': service,
    }

    return render(
        request,
        'review/review-create.html',
        context,
    )


@login_required
def review_edit(request, pk):
    review = Review.objects.filter(pk=pk).get()

    if review.reviewer == request.user:
        if request.method == 'GET':
            form = ReviewEditForm(instance=review)
        else:
            form = ReviewEditForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('catalogue')

        context = {
            'form': form,
            'review': review,
        }

        return render(
            request,
            'review/review-edit.html',
            context
        )

    return render(request, '403-forbidden-access.html')


@login_required
def review_delete_success(request):
    return render(
        request,
        'review/review-delete-success.html',
    )


@login_required
def recommendation_create(request):
    if request.method == 'GET':
        form = RecommendationCreateForm()
    else:
        form = RecommendationCreateForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = request.user
            rec.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        'about/recommendation-create.html',
        context
    )


@login_required
def recommendation_edit(request, pk):
    recommendation = Recommendation.objects.filter(pk=pk).get()

    if recommendation.user == request.user:
        if request.method == 'GET':
            form = RecommendationEditForm(instance=recommendation)
        else:
            form = RecommendationEditForm(request.POST, instance=recommendation)
            if form.is_valid():
                form.save()
                return redirect('details user', pk=request.user.pk)

        context = {
            'form': form,
            'recommendation': recommendation,
        }

        return render(
            request,
            'about/recommendation-edit.html',
            context
        )

    return render(request, '403-forbidden-access.html')


@login_required
def recommendation_delete(request, pk):
    recommendation = Recommendation.objects.filter(pk=pk).first()

    if recommendation.user == request.user:
        if request.method == 'GET':
            form = RecommendationDeleteForm(instance=recommendation)
        else:
            form = RecommendationDeleteForm(request.POST, instance=recommendation)
            if form.is_valid():
                form.save()
                return redirect('details user', pk=request.user.pk)

        context = {
            'form': form,
            'recommendation': recommendation,
        }

        return render(
            request,
            'about/recommendation-delete.html',
            context
        )

    return render(request, '403-forbidden-access.html')


@login_required
def announcement_create(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            form = AnnouncementCreateForm()
        else:
            form = AnnouncementCreateForm(request.POST)
            if form.is_valid():
                announcement = form.save(commit=False)
                announcement.date_posted = timezone.now()
                announcement.save()
                return redirect('index')

        context = {
            'form': form,
        }

        return render(
            request,
            'announcement/announcement-create.html',
            context
        )

    return render(request, '403-forbidden-access.html')


@login_required
def announcement_edit(request, pk):
    announcement = Announcement.objects.filter(pk=pk).get()

    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            form = AnnouncementEditForm(instance=announcement)
        else:
            form = AnnouncementEditForm(request.POST, instance=announcement)
            if form.is_valid():
                form.save()
                return redirect('index')

        context = {
            'form': form,
            'announcement': announcement,
        }

        return render(
            request,
            'announcement/announcement-edit.html',
            context
        )

    return render(request, '403-forbidden-access.html')


@login_required
def announcement_delete(request, pk):
    announcement = Announcement.objects.filter(pk=pk).get()

    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            form = AnnouncementDeleteForm(instance=announcement)
        else:
            form = AnnouncementDeleteForm(request.POST, instance=announcement)
            if form.is_valid():
                form.save()
                return redirect('index')

        context = {
            'form': form,
            'announcement': announcement,
        }

        return render(
            request,
            'announcement/announcement-delete.html',
            context
        )

    return render(request, '403-forbidden-access.html')


def handle_page_not_found_404(request, exception):
    return render(request, '404-page-not-found.html', status=404)
