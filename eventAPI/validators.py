from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def AllowPositiveDecimalValuesOnly(value):
    if value < 0:
        raise ValidationError(
            _(f"{value} is less than 0 you must put price bigger than 0 or 0 for a free ticket"),
            params={"value": value}
        )

def ticket_available_quantity_validator(value):
    if value <= 0:
        raise ValidationError(
            _(f"we don't have available tickets right now"),
            params={"value": value}
        )