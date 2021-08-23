from django.shortcuts import render
from events.models import Event, Venue

# Create your views here.
# Event.objects.order_by('-name')[:3]


def index(request):
    """ A view to show the index page """

    events = Event.objects.order_by('name')[:3]
    venues = Venue.objects.all()

    context = {
        'events': events,
        'venues': venues,
    }

    return render(request, 'home/index.html', context)
