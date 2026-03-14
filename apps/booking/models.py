from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Booking model to store customer reservations
class Booking(models.Model):
    # Choices for booking status
    STATUS_CHOICES = (
        # Booking created by the customer, waiting for staff approval
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),          # Booking approved by staff
        ('declined', 'Declined'),          # Booking declined/rejected by staff
        ('cancelled', 'Cancelled'),        # Booking cancelled by customer or staff
    )
    # Reference to the user who made the booking
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    # Current status of the booking
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True, null=True)

    # Timestamp when the booking was created automatically
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Human-readable representation of the booking
        return f"{self.customer.username} - {self.date} {self.time} ({self.status})"
