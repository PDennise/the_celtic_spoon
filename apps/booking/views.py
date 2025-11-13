from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required  # User must be logged in
def create_booking(request):                       
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user          # Automatically assign the logged-in user
            booking.save()
            return redirect('booking_success')       # Redirect after successful booking
        
    else: 
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form' : form})

