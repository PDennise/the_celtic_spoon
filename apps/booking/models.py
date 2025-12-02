from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Booking model to store customer reservations
class Booking(models.Model):
     # Choices for booking status
     STATUS_CHOICES = (
        ('pending', 'Pending Approval'),   # Booking created by the customer, waiting for staff approval
        ('approved', 'Approved'),          # Booking approved by staff
        ('declined', 'Declined'),          # Booking declined/rejected by staff
        ('cancelled', 'Cancelled'),        # Booking cancelled by customer or staff
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    customer = models.ForeignKey(User, on_delete=models.CASCADE) # Reference to the user who made the booking
    date = models.DateField()               # Date of the booking
    time = models.TimeField()               # Time of the booking
    number_of_guests = models.PositiveIntegerField() # Number of guests for the booking
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Current status of the booking


    created_at = models.DateTimeField(auto_now_add=True)    # Timestamp when the booking was created automatically

    def __str__(self):
        return f"{self.customer.username} - {self.date} {self.time} ({self.status})"    # Human-readable representation of the booking  