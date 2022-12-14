from django.urls import path, include

from music_services.web.views import index, service_create, service_edit, service_delete, ReviewCreateView, \
    ReviewDeleteView, recommendation_create, about, service_details, catalogue


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
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
