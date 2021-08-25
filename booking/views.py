from django.shortcuts import render, get_object_or_404
from events.models import Showtime
import json
# Create your views here.


def booking(request, showtime_id):
    """ A view to show the index page """

    showtime  = get_object_or_404(Showtime, pk=showtime_id)

    showtime_data = Showtime.objects.select_related().values('seating_plan').filter(pk=showtime_id)

    context = {
        'showtime': showtime,
        'showtime_data': json.dumps(list(showtime_data))
    }
    return render(request, 'booking/booking.html', context)
