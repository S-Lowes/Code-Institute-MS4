from django.shortcuts import render, get_object_or_404
from events.models import Showtime
from .forms import BookingForm
from django.http import JsonResponse
# Create your views here.

def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)
    seat_map = showtime.venue.seat_map
    seat_taken = showtime.seat_taken
    print(seat_taken)

    # AJAX Request
    if request.method == 'POST':
        data = request.POST
        st_cookie = data.get('seat_taken_cookie')
        split_st_cookie = st_cookie.split(",")
        new_st = seat_taken + split_st_cookie
        Showtime.objects.filter(pk=showtime_id).update(seat_taken=new_st)
        return JsonResponse({'status': 'Todo added!'})

    template = "booking/booking.html"

    context = {
        'showtime': showtime,
        'seat_map': seat_map,
        'seat_taken': seat_taken,

    }
    return render(request, template, context)


def payment(request, showtime_id):

    template = "booking/payment.html"

    return render(request, template)
