from django import forms
from .models import Booking

# Frontend form for users to make a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'date', 'time', 'number_of_guests']  # Fields user can fill
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),   # HTML5 date picker
            'time': forms.TimeInput(attrs={'type': 'time'}),   # HTML5 time picker
        }