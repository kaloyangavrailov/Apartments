from django.core.exceptions import ValidationError
from iso3166 import countries
def check_name_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')

def check_letters_only(value):
    if not value.isalpha():
        raise ValidationError('Your name must only contain letters!')

def check_numbers_letters_only(value):
    if not value.isalnum():
        raise ValidationError('Your name must only contain letters and numbers!')

def check_numbers_only(value):
    if not value.isdigit():
        raise ValidationError('Your name must only contain numbers!')

def check_valid_country(value):
    try:
        countries.get(value)
    except KeyError:
        raise ValidationError('Invalid country!')