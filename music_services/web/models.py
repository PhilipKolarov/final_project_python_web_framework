from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from music_services.accounts.models import AppUser


UserModel = get_user_model()


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
        to=UserModel,
        related_name='service_user',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
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


class Announcement(models.Model):
    MAX_LENGTH_TITLE = 50

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    info = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    date_posted = models.DateField(
        null=False,
        blank=False,
    )


class Review(models.Model):
    TERRIBLE = 1
    POOR = 2
    DESCENT = 3
    GREAT = 4
    EXCELLENT = 5

    RATING_TYPES = (
        (TERRIBLE, TERRIBLE),
        (POOR, POOR),
        (DESCENT, DESCENT),
        (GREAT, GREAT),
        (EXCELLENT, EXCELLENT),
    )

    reviewer = models.ForeignKey(
        to=UserModel,
        related_name='reviewer',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    reviewed_service = models.ForeignKey(
        to=Service,
        related_name='reviewed_service',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    rating = models.IntegerField(
        choices=RATING_TYPES,
        null=False,
        blank=False,
    )

    comment = models.TextField(
        null=False,
        blank=False,
    )


class Recommendation(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        related_name='recommender',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )
