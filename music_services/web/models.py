from django.core import validators
from django.db import models
from music_services.accounts.models import AppUser


class Service(models.Model):
    SESSION_MUSICIAN = 'Session Musician'
    AUDIO_ENGINEER = 'Audio Engineer'
    ARTIST_MANAGER = 'Artist Manager'
    MUSIC_PROMOTER = 'Music Promoter'
    OTHER = 'Other'

    SERVICE_TYPES = (
        (SESSION_MUSICIAN, SESSION_MUSICIAN),
        (AUDIO_ENGINEER, AUDIO_ENGINEER),
        (ARTIST_MANAGER, ARTIST_MANAGER),
        (MUSIC_PROMOTER, MUSIC_PROMOTER),
        (OTHER, OTHER),
    )

    MAX_LENGTH_TYPE = 30
    MAX_LENGTH_NAME = 128
    MIN_VALUE_PRICE = 1

    user = models.ForeignKey(
        AppUser, on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        choices=SERVICE_TYPES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_VALUE_PRICE)
        ],
        null=False,
        blank=False,
    )


class Achievements(models.Model):
    MAX_LENGTH_TITLE = 50

    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=200,
        null=True,
        blank=False,
    )


class Review(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    rating = models.IntegerField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )


class Recommendation(models.Model):
    description = models.TextField(
        null=False,
        blank=False,
    )
