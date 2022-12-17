from django.urls import path, include

from music_services.web.views import index, service_create, service_edit, service_delete, review_create, review_edit, \
    ReviewDeleteView, recommendation_create, about, service_details, catalogue, \
    review_delete_success, recommendation_edit, recommendation_delete, announcement_create, announcement_delete, \
    announcement_edit

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
    path('announcement/', include([
        path('create/', announcement_create, name='announcement create'),
        path('edit/<int:pk>', announcement_edit, name='announcement edit'),
        path('delete/<int:pk>', announcement_delete, name='announcement delete'),
    ])),
    path('review/', include([
        path('create/<int:pk>', review_create, name='review create'),
        path('edit/<int:pk>/', review_edit, name='review edit'),
        path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='review delete'),
        path('delete_success/', review_delete_success, name='review success'),

    ])),
    path('recommendation/', include([
        path('', recommendation_create, name='recommendation create'),
        path('edit/<int:pk>', recommendation_edit, name='recommendation edit'),
        path('delete/<int:pk>', recommendation_delete, name='recommendation delete'),
    ])),
]
