from django.shortcuts import render
from .models import MenuItem
from django.conf import settings

# Create your views here.
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu_list.html', {'items': items})

def contact(request):
    success = False  # to show success message in template

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        success = True  # send to template

    return render(request, 'contact.html', {'success': success})
