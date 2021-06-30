import datetime as dt

from django.core.exceptions import ValidationError


def date_validator(value):
    current_date = dt.date.today().year
    if value > current_date:
        raise ValidationError('Вы потаетесь созадть title из будущего')
