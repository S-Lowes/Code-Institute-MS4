from django.shortcuts import render, get_object_or_404
from events.models import Showtime
from .forms import BookingForm
from django.http import JsonResponse
# Create your views here.

import stripe


def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)
    seat_map = showtime.venue.seat_map
    seat_taken = showtime.seat_taken

    # AJAX Request
    if request.method == 'POST':
        data = request.POST
        st_cookie = data.get('seat_taken_cookie')
        split_st_cookie = st_cookie.split(",")
        new_st = seat_taken + split_st_cookie
        Showtime.objects.filter(pk=showtime_id).update(seat_taken=new_st)
        return JsonResponse({'status': 'Todo added!'})

    template = "booking/booking.html"

    form = BookingForm()

    context = {
        'form': form,
        'showtime': showtime,
        'seat_map': seat_map,
        'seat_taken': seat_taken,
        'stripe_public_key':'pk_test_51J22ppHHOtvYgnT9zBxZ1XMFKv5aDIjmfUc1mY2vxjsEduh6bTERlNDP1rPvjRatRWHZP2csTBpXVfeGyZopbICU00EvwQM8qD',
        'client_secret': 'test',

    }
    return render(request, template, context)
