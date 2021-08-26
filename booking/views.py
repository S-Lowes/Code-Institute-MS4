from django.shortcuts import render, get_object_or_404
from events.models import Showtime
import json
# Create your views here.


def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)

    seat_map = showtime.venue.seat_map

    context = {
        'showtime': showtime,
        'seat_map': seat_map
    }
    return render(request, 'booking/booking.html', context)
