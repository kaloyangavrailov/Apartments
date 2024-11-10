from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from bookings_website.validators import check_letters_only, check_numbers_letters_only, \
    check_numbers_only, check_name_capital_letter, check_valid_country


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null= False,
        blank= False,
        validators=[MinLengthValidator(2), check_numbers_letters_only]
    )

    email = models.EmailField(
        null= False,
        blank= False,
    )

    phone = models.IntegerField(
        null= False,
        blank= False,
        validators=[check_numbers_only]
    )

    address = models.TextField(
        null= False,
        blank= False,
        max_length=150,
    )

    first_name = models.CharField(
        null= False,
        blank= False,
        max_length=30,
        validators=[check_letters_only, check_name_capital_letter],
    )

    last_name = models.CharField(
        null= False,
        blank= False,
        validators=[check_letters_only, check_name_capital_letter],
        max_length=30,
    )

    country = models.CharField(
        null= False,
        blank= False,
        validators=[check_valid_country],
        max_length=50
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

class Apartment(models.Model):
    name = models.CharField(
        null= False,
        blank= False,
        max_length=50,
        validators=[MinLengthValidator(10), check_letters_only],
    )

    address = models.TextField(
        null= False,
        blank= False,
        max_length=150,
    )

    beds = models.IntegerField(
        null= False,
        blank= False,
        validators=[MinValueValidator(1)],
    )

    rooms = models.IntegerField(
        null= False,
        blank= False,
        validators=[MinValueValidator(1)],
    )

    max_occupancy = models.IntegerField(
        null= False,
        blank= False,
        validators=[MinValueValidator(1)],
    )

    price = models.IntegerField(
        null= False,
        blank= False,
    )

    contact_phone = models.IntegerField(
        null= False,
        blank= False,
        validators=[check_numbers_only]
    )

    contact_email = models.EmailField(
        null= False,
        blank= False,
    )

    owner_first_name = models.CharField(
        null= False,
        blank= False,
        max_length=15,
        validators=[MinLengthValidator(2), check_letters_only, check_name_capital_letter],

    )

    owner_last_name = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=[MinLengthValidator(2), check_letters_only, check_name_capital_letter],
    )

class Review(models.Model):
    reviewer_id = models.ManyToManyField(Profile)
    date = models.DateField(
        null= False,
        blank= False,
    )
    apartment_id = models.ManyToManyField(Apartment)
    text = models.TextField(
        null= False,
        blank= False,
        max_length=300,
    )
    score = models.IntegerField(
        null= False,
        blank= False,
        validators=[MaxValueValidator(10), MinValueValidator(1)],
    )

class Reservation(models.Model):
    apartment_id = models.OneToOneField(Apartment, on_delete=models.CASCADE, primary_key=True)

    check_in = models.DateField(
        null= False,
        blank= False,
    )

    check_out = models.DateField(
        null= False,
        blank= False,
    )

    number_guests = models.IntegerField(
        null= False,
        blank= False,
        validators=[MinValueValidator(1)],
    )

    price_per_night = models.IntegerField(
        null= False,
        blank= False,
    )

    guest_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Blacklist(models.Model):
    guest_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    reason = models.TextField(
        max_length=300,
    )