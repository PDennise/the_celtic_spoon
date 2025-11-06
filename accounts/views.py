from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Django built-in forms for user signup and login
from django.contrib.auth import login, logout # Functions to log users in and out

# Create your views here.
def register_view(request):
    form = UserCreationForm()                       # Create an empty user registration form
    if request.method == 'POST':                    # Check if the form was submitted
        form = UserCreationForm(request.POST)       # Bind POST data to the form
        if form.is_valid():                         # Validate the form data
            user = form.save()                      # Save the new user to the database
            login(request, user)                    # Log the user in immediately
            return redirect('/')                    # Redirect to the homepage after successful registration
    return render(request, 'accounts/register.html', {'form' : form}) # Render the registration template with the form (either empty or with errors)

