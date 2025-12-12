from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from apps.booking.models import Booking
from django.contrib import messages

# Only staff users can access
@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    bookings = Booking.objects.all().order_by('-date') # get all bookings
    context = {
        'bookings': bookings
    }

    return render(request, 'staff_dashboard.html', context)

@user_passes_test(lambda u: u.is_staff)
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'approved'
    booking.save()
    messages.success(request, f"Booking #{booking.id} approved.")
    return redirect('staff_dashboard')

@user_passes_test(lambda u: u.is_staff)
def decline_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'declined'
    booking.save()
    messages.success(request, f"Booking #{booking.id} declined.")
    return redirect('staff_dashboard')

@user_passes_test(lambda u: u.is_staff)
def complete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'complete'
    booking.save()
    messages.success(request, f"Booking #{booking_id} marked as completed.")
    return redirect('staff_dashboard')

def home_view(request):
    return render(request, 'home.html')
