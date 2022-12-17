from django.contrib.auth.models import AbstractUser
from django.db import models

from music_services.accounts.validators import username_length_validator, name_validator


class AppUser(AbstractUser):
    MAX_LENGTH_USERNAME = 30
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_NAME = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            username_length_validator
        ],
        unique=True,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(
            name_validator,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(
            name_validator,
        ),
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
