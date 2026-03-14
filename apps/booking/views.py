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
            form.save()
            # Success message
            messages.success(
                request, "Your booking has been successfully created!"
                )

            return redirect('my_bookings')  # Redirect to user's bookings page
    else:
        form = BookingForm(user=request.user)
    return render(request, 'booking/create_booking.html', {'form': form})


# View to list all bookings of the current user (staff use dashboard instead)
@login_required
def my_bookings(request):
    if request.user.is_staff:
        return redirect('staff_dashboard')
    bookings = Booking.objects.filter(
        customer=request.user).order_by('-date', '-time')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})


def _get_booking_for_request(request, pk):
    """Staff can view any booking; customers only their own."""
    if request.user.is_staff:
        return get_object_or_404(Booking, pk=pk)
    return get_object_or_404(Booking, pk=pk, customer=request.user)


# View to booking details
@login_required
def booking_detail(request, pk):
    booking = _get_booking_for_request(request, pk)
    return render(request, 'booking/booking_detail.html', {'booking': booking})


@login_required
def update_booking(request, pk):
    booking = _get_booking_for_request(request, pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your booking has been updated successfully!",
            )
            return redirect(
                'staff_dashboard' if request.user.is_staff else 'my_bookings'
            )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = BookingForm(instance=booking, user=request.user)

    return render(request, 'booking/update_booking.html', {'form': form})


@login_required
def delete_booking(request, pk):
    booking = _get_booking_for_request(request, pk)

    if request.method == "POST":
        booking.delete()
        messages.success(
            request,
            "Your booking has been deleted successfully.",
        )
        return redirect(
            "staff_dashboard" if request.user.is_staff else "my_bookings"
        )

    return render(request, "booking/delete_booking.html", {"booking": booking})
