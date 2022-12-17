from django.core.exceptions import ValidationError

from music_services.accounts.utils import includes_number


def username_length_validator(username):
    if len(username) < 4:
        raise ValidationError("The username must be at least 4 characters long.")


def name_validator(name):
    if len(name) < 1:
        raise ValidationError("Names should contain at least one character.")
    if includes_number(name):
        raise ValidationError("Names cannot contain numbers.")

