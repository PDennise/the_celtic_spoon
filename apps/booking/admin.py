from django.contrib import admin
from django import forms
from .models import Booking
# Register your models here.


class BookingAdminForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),

        }


class BookingAdmin(admin.ModelAdmin):   # Admin configuration for Booking model
    form = BookingAdminForm
    list_display = (
        'customer',
        'date',
        'time',
        'number_of_guests',
        'status',
        'created_at')      # Columns to display in admin list view


admin.site.register(Booking, BookingAdmin)
# Register Booking model with the custom admin configuration
