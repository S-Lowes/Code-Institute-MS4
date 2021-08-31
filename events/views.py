from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Event, Showtime, Venue
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
    showtimes = Showtime.objects.select_related().filter(event=event_id).order_by('date')

    context = {
        'showtimes': showtimes,
        'event': event,
    }

    return render(request, 'events/showtimes.html', context)


@login_required
def event_management(request):
    """ Event Management Menu """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    template = "events/event_management.html"

    return render(request, template)


@login_required
def add_event(request):
    """ Create an event """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added an event!')
            return redirect(reverse('add_event'))
        else:
            messages.error(request, 'Failed to add the event. Please ensure the form is valid.')
    else:
        form = EventForm()

    template = "events/add_event.html"

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_venue(request):
    """ Create a venue """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save()
            messages.success(request, 'Successfully added a venue!')
            return redirect(reverse('add_venue'))
        else:
            messages.error(request, 'Failed to add the venue. Please ensure the form is valid.')
    else:
        form = VenueForm()

    template = "events/add_venue.html"

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_showtime(request):
    """ Create an event showtime """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ShowtimeForm(request.POST)
        if form.is_valid():
            showtime = form.save()
            messages.success(request, 'Successfully added a showtime!')
            return redirect(reverse('add_showtime'))
        else:
            messages.error(request, 'Failed to add the showtime. Please ensure the form is valid.')
    else:
        form = ShowtimeForm()

    template = "events/add_showtime.html"

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit an event """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('event_management'))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.name}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


@login_required
def edit_venue(request, venue_id):
    """ Edit a venue """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    venue = get_object_or_404(Venue, pk=venue_id)
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated venue!')
            return redirect(reverse('event_management'))
        else:
            messages.error(request, 'Failed to update venue. Please ensure the form is valid.')
    else:
        form = VenueForm(instance=venue)
        messages.info(request, f'You are editing {venue.name}')

    template = 'events/edit_venue.html'
    context = {
        'form': form,
        'venue': venue,
    }

    return render(request, template, context)


@login_required
def edit_showtime(request, showtime_id):
    """ Edit an event showtime """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    showtime = get_object_or_404(Showtime, pk=showtime_id)
    if request.method == 'POST':
        form = ShowtimeForm(request.POST, request.FILES, instance=showtime)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated showtime!')
            return redirect(reverse('event_management'))
        else:
            messages.error(request, 'Failed to update showtime. Please ensure the form is valid.')
    else:
        form = ShowtimeForm(instance=showtime)
        messages.info(request, f'You are editing {showtime.name}')

    template = 'events/edit_showtime.html'
    context = {
        'form': form,
        'showtime': showtime,
    }

    return render(request, template, context)
