from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import date, time

# Frontend form for users to make a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # We'll add the 'time' field manually in __init__
        fields = ['date', 'number_of_guests']  # Fields user can fill
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),   # HTML5 date picker
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        error_messages = {
            # Custom error messages for the 'date' field
            'date': {
                'required': "Please select a date.",     # Shown when field is empty
                'invalid': "Please enter a valid date.", # Shown when invalid input format is given
            },
            # Custom error messages for the 'number_of_guests' field
            'number_of_guests': {
                'required': "Please enter number of guests.",  # Shown when no value is provided
            }
        }


    def __init__(self, *args, **kwargs):
        # to access request.user inside the form
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Create time slots with 15-minute intervals
        time_choices = []
        # Generate times from 12:00 to 21:45 (restaurant hours)
        for hour in range(12, 22):  # 12:00 to 21:45
            for minute in (0, 15, 30, 45):
                time_str = f"{hour:02d}:{minute:02d}"
                time_display = f"{hour:02d}:{minute:02d}"
                time_choices.append((time_str, time_display))
        
        # Add time field as a ChoiceField (dropdown)
        self.fields['time'] = forms.ChoiceField(
            choices=time_choices,
            widget=forms.Select(attrs={'class': 'form-control'}),
            label="Time",
            required=True
        )

        # Reorder fields to show: Date, Time, Number of Guests
        self.order_fields(['date', 'time', 'number_of_guests'])

    
    def save(self, commit=True):
        """Override save to set the time field from cleaned_data"""
        instance = super().save(commit=False)
        
        # Set time from cleaned_data (converted in clean_time())
        if 'time' in self.cleaned_data:
            instance.time = self.cleaned_data['time']
        
        # Set customer if available
        if self.user:
            instance.customer = self.user
        
        if commit:
            instance.save()
        
        return instance

    def clean_number_of_guests(self):
        guests = self.cleaned_data.get('number_of_guests')
        if guests is None:
            raise forms.ValidationError("Please enter number of guests.")
        if guests < 1:
            raise forms.ValidationError("Number of guests must be at least 1.")
        if guests > 20:  
            raise forms.ValidationError("We cannot accommodate more than 20 guests per booking.")
        return guests


    def clean_time(self):
        """Convert time string from dropdown to time object"""
        time_str = self.cleaned_data.get('time')
        if not time_str:
            raise forms.ValidationError("Please select a time.")

        # Convert string "HH:MM" to time object
        hour, minute = map(int, time_str.split(':'))
        time_value = time(hour, minute)
        
        # Check capacity if date is provided
        date_value = self.cleaned_data.get('date')
        if date_value:
            max_bookings_per_slot = 20
            
            existing_bookings = Booking.objects.filter(
                date=date_value,
                time=time_value
            ).count()
            
            if existing_bookings >= max_bookings_per_slot:
                raise forms.ValidationError(
                    f"Sorry, {time_value.strftime('%H:%M')} on {date_value} is fully booked. "
                    f"Please choose another time."
                )
        
        return time_value


    def clean_date(self):
        date_value = self.cleaned_data.get('date')
        if date_value is None:
            raise ValidationError("Please enter a valid date")
        if date_value < date.today():
            raise ValidationError("You cannot select a past date.")
        return date_value
    
    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time = cleaned_data.get('time')

        if booking_date and booking_time and self.user:
            # Check if user already has a booking at this date and time
            if Booking.objects.filter(customer=self.user, date=booking_date, time=booking_time).exists():
                raise ValidationError("You already have a booking at this date and time.")

        return cleaned_data