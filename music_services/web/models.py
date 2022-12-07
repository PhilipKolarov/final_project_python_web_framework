from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def username_length_validator(username):
    if len(username) < 4:
        raise ValidationError("The username must be at least 4 characters long")


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 25
    MAX_LENGTH_PASSWORD = 25
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            username_length_validator,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    # TODO check if this is appropriate
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

#TODO Attach to Profile by using 'user = models.ForeignKey(Profile, on_delete=models.CASCADE)
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
    MIN_VALUE_PRICE = 1

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

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

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
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    rating = models.IntegerField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )


