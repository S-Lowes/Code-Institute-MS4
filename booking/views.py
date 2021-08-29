from django.views import View
from django.shortcuts import render, get_object_or_404
from events.models import Showtime
from .forms import BookingForm
from django.http import JsonResponse
from django.conf import settings
# Create your views here.

import stripe


def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)
    seat_map = showtime.venue.seat_map
    seat_taken = showtime.seat_taken
    ticket_price = showtime.ticket_price

    # AJAX Request
    # if request.method == 'POST':
    #     data = request.POST
    #     st_cookie = data.get('seat_taken_cookie')
    #     sn_cookie = data.get('seat_number_cookie')
    #     print(st_cookie, sn_cookie)

    #     split_st_cookie = st_cookie.split(",")
    #     new_st = seat_taken + split_st_cookie
    #     print(new_st)
    #     # Showtime.objects.filter(pk=showtime_id).update(seat_taken=new_st)
    #     return JsonResponse({'status': 'Todo added!'})

    template = "booking/booking.html"

    form = BookingForm()

    context = {
        'form': form,
        'showtime': showtime,
        'seat_map': seat_map,
        'seat_taken': seat_taken,
        'ticket_price': ticket_price,

    }
    return render(request, template, context)


def payment(request, showtime_id):

    showtime = get_object_or_404(Showtime, pk=showtime_id)
    form = BookingForm()
    cost_per_ticket = int(showtime.ticket_price)
    print(cost_per_ticket)

    seat_taken_data = showtime.seat_taken

    st_cookie = request.COOKIES.get('cookie_seating')
    sn_cookie = request.COOKIES.get('cookie_number')
    list_st_cookie = st_cookie.split(",")
    list_sn_cookie = sn_cookie.split(",")

    if set(seat_taken_data).intersection(set(list_st_cookie)):
        print("These lists contain some identical elements.")
    else:
        print("These lists do NOT contain identical elements.")

    if len(list_st_cookie) != len(list_sn_cookie):
        print("These lists are same length")
    else:
        print("These lists are NOT same length")

    number_of_tickets = len(list_st_cookie)

    total_cost = number_of_tickets * cost_per_ticket

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe_total = round(int(total_cost)*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )

    template = "booking/payment.html"

    context = {
        'form': form,
        'showtime': showtime,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
