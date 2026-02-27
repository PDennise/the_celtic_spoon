from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name= 'create_booking'),  #  # URL for creating a booking
    path('my-bookings/', views.my_bookings, name='my_bookings'),          # View user's bookings
    path('<int:pk>/', views.booking_detail, name='booking_detail'), # View user's booking details
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),  # Cancel a booking
    path('<int:pk>/edit/', views.update_booking, name='update_booking'), # Update (Edit) booking
    path('<int:pk>/delete/', views.delete_booking, name='delete_booking'), # Delete booking
]