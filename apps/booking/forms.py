from django import forms
from .models import Booking

# Frontend form for users to make a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'date', 'time', 'number_of_guests']  # Fields user can fill
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),   # HTML5 date picker
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),   # HTML5 time picker
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }