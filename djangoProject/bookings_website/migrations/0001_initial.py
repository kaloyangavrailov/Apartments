# Generated by Django 5.1.3 on 2024-11-26 13:27

import bookings_website.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(10), bookings_website.validators.check_letters_only])),
                ('address', models.TextField(max_length=150)),
                ('beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('rooms', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('max_occupancy', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.IntegerField()),
                ('contact_phone', models.IntegerField(validators=[bookings_website.validators.check_numbers_only])),
                ('contact_email', models.EmailField(max_length=254)),
                ('owner_first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), bookings_website.validators.check_letters_only, bookings_website.validators.check_name_capital_letter])),
                ('owner_last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), bookings_website.validators.check_letters_only, bookings_website.validators.check_name_capital_letter])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), bookings_website.validators.check_numbers_letters_only])),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(validators=[bookings_website.validators.check_numbers_only])),
                ('address', models.TextField(max_length=150)),
                ('first_name', models.CharField(max_length=30, validators=[bookings_website.validators.check_letters_only, bookings_website.validators.check_name_capital_letter])),
                ('last_name', models.CharField(max_length=30, validators=[bookings_website.validators.check_letters_only, bookings_website.validators.check_name_capital_letter])),
                ('country', models.CharField(max_length=50, validators=[bookings_website.validators.check_valid_country])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=300)),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('apartment_id', models.ManyToManyField(to='bookings_website.apartment')),
                ('reviewer_id', models.ManyToManyField(to='bookings_website.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('apartment_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bookings_website.apartment')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('number_guests', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price_per_night', models.IntegerField()),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings_website.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=300)),
                ('apartment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings_website.apartment')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings_website.profile')),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings_website.reservation')),
            ],
        ),
    ]