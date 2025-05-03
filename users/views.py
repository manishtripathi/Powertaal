from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models.models import FreeUser
from users.models.advanceuser import AdvanceUser

from django.utils import timezone
import random

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.CreatedDate = timezone.now()
            user.CreatedBySource = 'Website'
            user.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def guest_login(request):
    guest_name = "Guest_" + str(random.randint(1000, 9999))
    guest = FreeUser(
        UserName=guest_name,
        Place='Guest',
        CreatedDate=timezone.now(),
        CreatedBySource='GuestLogin'
    )
    guest.save()
    # Redirect or login session creation after guest creation
    return redirect('success_page')

def success_page(request):
    return render(request, 'success.html')

def show_advance_users(request):
    users = AdvanceUser.objects.all()
    return render(request, 'users/advance_users.html', {'users': users})

