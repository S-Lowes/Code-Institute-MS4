from django.shortcuts import render, get_object_or_404
from events.models import Showtime, Venue

# Create your views here.
# Event.objects.order_by('-name')[:3]


def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = showtime = get_object_or_404(Showtime, pk=showtime_id)

    context = {
        'showtime': showtime,
    }
    return render(request, 'booking/booking.html', context)
