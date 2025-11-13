from django.urls import path
from . import views

urlpatterns [
    path('create/', views.create_booking, name= 'create_booking'),  #  # URL for creating a booking
]