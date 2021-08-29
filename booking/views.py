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
    print(seat_taken)

    # AJAX Request
    if request.method == 'POST':
        data = request.POST
        total = data.get('total_recalc')
        seat_id = data.get('id_recalc')
        seat_label = data.get('label_recalc')

        request.session['total'] = total
        request.session['seat_id'] = seat_id
        request.session['seat_label'] = seat_label
        return JsonResponse({'status': 'Data Acquired By View!'})

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

    booking_form = BookingForm()
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    total = request.session['total']
    seat_id = request.session['seat_id']
    seat_label = request.session['seat_label']

    print(seat_id, seat_label)

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe_total = round(int(total)*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )

    template = "booking/payment.html"

    context = {
        'booking_form': booking_form,
        'showtime': showtime,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
