from django.urls import path,include
from bookings_website import views
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
    path('reviews/', include([
        path('', views.reviews_catalogue, name='reviews_catalogue'),
        path('write/', views.review_write, name='review_write'),
        path('edit/', views.review_edit, name='review_edit'),
        path('delete/', views.review_delete, name='review_delete'),
    ])),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]

