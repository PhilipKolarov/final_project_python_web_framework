from django.urls import path, include

from music_services.web.views import index, ProfileCreateView, ProfileDeleteView, ProfileEditView, service_create, \
    service_edit, service_delete, ReviewCreateView, ReviewDeleteView, recommendation_create, about, service_details, \
    ProfileDetailsView, catalogue

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('profile/', include([
        path('create/', ProfileCreateView.as_view(), name='profile create'),
        path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
    path('catalogue', catalogue, name='catalogue'),
    path('service/', include([
        path('create/', service_create, name='service create'),
        path('details/<int:pk>/', service_details, name='service details'),
        path('edit/<int:pk>/', service_edit, name='service edit'),
        path('delete/<int:pk>/', service_delete, name='service delete'),
    ])),
    path('review/', include([
        path('create/', ReviewCreateView.as_view(), name='review create'),
        path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='review delete'),
    ])),
    path('recommendation/', recommendation_create, name='recommendation create'),
]
