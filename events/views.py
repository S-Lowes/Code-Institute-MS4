from django.shortcuts import render, get_object_or_404
from .models import Event, Showtime
# Create your views here.


def all_events(request):
    """ A view to show all events including search query """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)


def event_showtimes(request, event_id):
    """ A view to show individual event showtimes """

    event = get_object_or_404(Event, pk=event_id)
    showtimes = Showtime.objects.select_related().filter(event=event_id)

    context = {
        'showtimes': showtimes,
        'event': event,
    }

    return render(request, 'events/showtimes.html', context)
