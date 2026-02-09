from django.core.exceptions import ValidationError


def validate_file_size(value):
    if value.size > 5242880:
        raise ValidationError("The maximum upload size is 5MB.")

