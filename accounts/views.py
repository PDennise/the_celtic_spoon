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
            messages.success(request, "Account created successfully!")
            return redirect('home')                    # Redirect to the homepage after successful registration
        else:
            messages.error(request, "Please correcr the errors below.")  
    return render(request, 'accounts/register.html', {'form' : form}) # Render the registration template with the form (either empty or with errors)


def login_view(request):
    form = AuthenticationForm()                     # Create an empty login form for GET requests
    if request.method == 'POST':                    # Check if the form has been submitted
        form = AuthenticationForm(request, data=request.POST) # Bind POST data to the form
        if form.is_valid():                         # Validate the form (check username and password)
            user = form.get_user()                  # Get the authenticated user object
            login(request, user)                    # Log the user in (start a session)
            return redirect('home')                 # Redirect to the homepage after successful login
    return render(request, 'accounts/login.html', {'form': form}) #  Render the login template with the form (empty or with errors)


def logout_view(request):
    logout(request)  # Log the user out (end the session)
    return redirect('/')  # Redirect to the homepage after logout
