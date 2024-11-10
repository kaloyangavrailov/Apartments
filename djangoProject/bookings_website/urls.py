from django.urls import path,include
from bookings_website import views

"""
	http://localhost:8000/ - home page
	http://localhost:8000/apartments-catalogue - apartment catalogue page
	
	http://localhost:8000/apartment-details - apartment details page
	
	http://localhost:8000/reservations - reservations page
	http://localhost:8000/reservations/edit - reservation edit page
	http://localhost:8000/reservations/delete - reservation delete page
	http://localhost:8000/reservations/details - reservation details page
	
	http://localhost:8000/profile/create - profile create page
	http://localhost:8000/profile/details - profile details page
	http://localhost:8000/profile/edit - profile edit page
	http://localhost:8000/profile/delete - profile delete page
	
	http://localhost:8000/reviews - reviews page
	http://localhost:8000/reviews/write - reviews write page
	http://localhost:8000/reviews/edit - edit reviews page
	http://localhost:8000/reviews/delete -delete reviews page
	
	http://localhost:8000/contact
	
	http://localhost:8000/about
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('apartments-catalogue/', views.apartments_catalogue, name='apartments-catalogue'),
    path('apartment-details/', views.apartment_details, name='apartment-details'),
    path('reservations/', include([
        path('', views.reservations, name='reservations'),
        path('edit/', views.reservations_edit, name='reservations_edit'),
        path('delete/', views.reservations_delete, name='reservations_delete'),
    ])),
    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]