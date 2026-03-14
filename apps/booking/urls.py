from django.urls import path

from . import views

urlpatterns = [
    # URL for creating a booking
    path('create/', views.create_booking, name='create_booking'),
    # View user's bookings
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    # View user's booking details
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    # Update (Edit) booking
    path('<int:pk>/edit/', views.update_booking, name='update_booking'),
    # Delete booking
    path('<int:pk>/delete/', views.delete_booking, name='delete_booking'),
]
