from django.core.exceptions import ValidationError


def check_if_username_is_acceptable(username):
    for char in username:
        if not char.isalnum() and char != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")