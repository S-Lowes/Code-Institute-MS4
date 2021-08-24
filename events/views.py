from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Event, Showtime
from .forms import EventForm, VenueForm, ShowtimeForm

# Create your views here.


def all_events(request):
    """ A view to show all events including search query """

    events = Event.objects.all()
    query = None

    if 'search' in request.GET:
        query = request.GET['search']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('events'))

        queries = Q(name__icontains=query) | Q(description_short__icontains=query) | Q(description_long__icontains=query)
        events = events.filter(queries)

    context = {
        'events': events,
        'search_term': query,
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


def add_event(request):
    """ Create an event """

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_event'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = EventForm()

    template = "events/add_event.html"

    context = {
        'form': form,
    }

    return render(request, template, context)


def add_venue(request):
    """ Create a venue """

    form = VenueForm()
    template = "events/add_venue.html"

    context = {
        'form': form,
    }

    return render(request, template, context)


def add_showtime(request):
    """ Create an event showtime """

    form = ShowtimeForm()
    template = "events/add_showtime.html"

    context = {
        'form': form,
    }

    return render(request, template, context)
