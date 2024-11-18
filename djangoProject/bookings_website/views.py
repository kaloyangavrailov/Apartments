from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request, 'common/homepage.html')

def apartments_catalogue(request):
    return render(request, 'apartment/apartment-catalogue.html')

def apartment_details(request):
    return render(request, 'apartment/apartment-page.html')

def reservations(request):
    return render(request, 'reservation/reservations-catalogue.html')

def reservations_edit(request):
    return render(request, 'reservation/reservation-make-edit-delete.html')

def reservations_delete(request):
    return render(request, 'reservation/reservation-make-edit-delete.html')

def profile_create(request):
    return render(request, 'profile/profile-login-signup.html')

def profile_log_in(request):
    return render(request, 'profile/profile-login-signup.html')

def profile_details(request):
    return render(request, 'profile/profile-details.html')

def profile_edit(request):
    return render(request, 'profile/profile-edit-delete.html')

def profile_delete(request):
    return render(request, 'profile/profile-edit-delete.html')

def reviews_catalogue(request):
    return render(request, 'reviews/reviews-catalogue.html')

def review_write(request):
    return render(request, 'reviews/review-write-edit-delete.html')

def review_edit(request):
    return render(request, 'reviews/review-write-edit-delete.html')

def review_delete(request):
    return render(request, 'reviews/review-write-edit-delete.html')

def contact(request):
    return render(request, 'common/contact.html')

def about(request):
    return render(request, 'common/about.html')
