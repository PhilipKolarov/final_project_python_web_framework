from django.urls import path, include

from music_services.web.views import index, ProfileCreateView, ProfileDeleteView, ProfileEditView, ServicesCreateView, \
    ServicesEditView, ServicesDeleteView, ReviewCreateView, ReviewDeleteView, recommendation_create

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('profile/', include([
        path('create/', ProfileCreateView.as_view(), name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
    path('services/', include([
        path('', services, name='services'),
        path('create/', ServicesCreateView.as_view(), name='services create'),
        path('details/<int:pk>/', services_details, name='services details'),
        path('edit/<int:pk>/', ServicesEditView.as_view(), name='services edit'),
        path('delete/<int:pk>/', ServicesDeleteView.as_view(), name='services delete'),
    ])),
    path('review/', include([
        path('create/', ReviewCreateView.as_view(), name='review create'),
        path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='review delete'),
    ])),
    path('recommendation/', recommendation_create, name='recommendation create'),
]
