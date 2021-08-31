from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profiles(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact number updated successfully')

    form = UserProfileForm(instance=profile)
    bookings = profile.booking.all()

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'bookings': bookings
    }

    return render(request, template, context)
