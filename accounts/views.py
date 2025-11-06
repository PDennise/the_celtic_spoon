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
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html', {'form': form})