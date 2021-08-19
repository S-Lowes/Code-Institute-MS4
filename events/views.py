from django.shortcuts import render
from .models import Event
# Create your views here.


def all_events(request):
    """ A view to show all events including search query """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)
