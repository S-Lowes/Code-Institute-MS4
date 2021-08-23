from django.shortcuts import render
from events.models import Showtime, Venue

# Create your views here.
# Event.objects.order_by('-name')[:3]


def booking(request):
    """ A view to show the index page """

    showtime = Showtime.objects.all()
    venues = Venue.objects.all()

    context = {
        'showtime': showtime,
        'venues': venues,
    }
    return render(request, 'booking/booking.html', context)
