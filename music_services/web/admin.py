from django.contrib import admin

from music_services.web.models import Service, Achievements, Review, Recommendation


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    pass
