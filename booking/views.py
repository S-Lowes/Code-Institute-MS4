from django.shortcuts import render, get_object_or_404
from events.models import Showtime, Venue
import json
# Create your views here.


def booking(request, showtime_id, venue_id):
    """ A view to show the index page """

    showtime  = get_object_or_404(Showtime, pk=showtime_id)
    venue  = get_object_or_404(Venue, pk=venue_id)

    context = {
        'showtime': showtime,
        'venue': venue
    }
    return render(request, 'booking/booking.html', context)
