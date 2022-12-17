from django.contrib import admin

from music_services.web.models import Service, Announcement, Review, Recommendation


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'price',)
    list_filter = ('type', 'date_added',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_filter = ('date_posted',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'reviewed_service',)
    list_filter = ('rating', 'date',)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    pass
