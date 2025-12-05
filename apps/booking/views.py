from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking

# View to create a new booking
@login_required  # User must be logged in
def create_booking(request):                       
    if request.method == 'POST':
        # Pass request.user to the form for validation
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            # Don't save to DB yet, we need to assign the customer
            booking = form.save()
            # Success message
            messages.success(request, "Your booking has been successfully created!")
            
            return redirect('my_bookings')       # Redirect to user's bookings page
        
    else: 
        form = BookingForm(user=request.user)
    return render(request, 'booking/create_booking.html', {'form' : form})


# View to list all bookings of the current user
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer=request.user).order_by('-date', '-time')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})


# View to cancel a booking
@login_required
def cancel_booking(request, booking_id):
    # Get booking or return 404 if not found or not owned by user
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    
    if booking.status in ['approved', 'pending']:
        booking.status = 'cancelled'  # Update status
        booking.save()
        messages.success(request, "Your booking has been cancelled successfully.")
    else:
        messages.warning(request, "This booking cannot be cancelled.")

    return redirect('my_bookings')