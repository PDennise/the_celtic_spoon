from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from apps.booking.models import Booking

# Only staff users can access
@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    bookings = Booking.objects.all().order_by('-date') # get all bookings
    context = {
        'bookings': bookings
    }

    return render(request, 'staff_dashboard.html', context)

def home_view(request):
    return render(request, 'home.html')
