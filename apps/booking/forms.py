from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import time as datetime_time

# Frontend form for users to make a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_guests']  # Fields user can fill
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),   # HTML5 date picker
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),   # HTML5 time picker
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }


    def __init__(self, *args, **kwargs):
        # to access request.user inside the form
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


    def clean_number_of_guests(self):
        guests = self.cleaned_data.get('number_of_guests')
        if guests < 1:
            raise forms.ValidationError("Number of guests must be at least 1.")
        if guests > 20:  # Example capacity limit
            raise forms.ValidationError("We cannot accommodate more than 20 guests per booking.")
        return guests

    
     def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time = cleaned_data.get('time')

        if booking_date and booking_time and self.user:
            # Check if user already has a booking at this date and time
            if Booking.objects.filter(customer=self.user, date=booking_date, time=booking_time).exists():
                raise ValidationError("You already have a booking at this date and time.")

            # Check business hours (example: 12:00 - 22:00)
            if not (datetime_time(12, 0) <= booking_time <= datetime_time(22, 0)):
                raise ValidationError("Booking time must be between 12:00 and 22:00.")

        return cleaned_data