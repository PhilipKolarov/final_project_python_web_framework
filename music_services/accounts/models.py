from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def includes_number(string):
    return any(ch.isdigit() for ch in string)


def username_length_validator(username):
    if len(username) < 4:
        raise ValidationError("The username must be at least 4 characters long.")


def password_validator(password):
    if len(password) < 4:
        raise ValidationError("The password must be at least 4 characters long.")
    if not includes_number(password):
        raise ValidationError("The password must include at least one number.")
    if password.isdigit():
        raise ValidationError("The password must include at least one letter.")


def name_validator(name):
    if len(name) < 1:
        raise ValidationError("Names should contain at least one character.")
    if includes_number(name):
        raise ValidationError("Names cannot contain numbers.")


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
