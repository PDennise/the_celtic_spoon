from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
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
            booking = form.save(commit=False)
            booking.customer = request.user          # Automatically assign the logged-in user
            booking.save()                           # Now save to DB
            return redirect('my_bookings')       # Redirect to user's bookings page
        
    else: 
        form = BookingForm(user=request.user)
    return render(request, 'booking/create_booking.html', {'form' : form})


# View to list all bookings of the current user
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer=request.user).order_by('-date', '-time')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
