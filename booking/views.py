from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import Booking
from events.models import Showtime
from .forms import BookingForm

import stripe
# Create your views here.


def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)

    seat_map = showtime.venue.seat_map
    seat_taken = showtime.seat_taken
    ticket_price = showtime.ticket_price

    print(seat_map)
    print(type(seat_map))


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

    context = {
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

    list_seat_id = seat_id.lstrip("[").rstrip("]").replace('"', '').split(",")
    list_seat_label = seat_label.lstrip("[").rstrip("]").replace('"', '').split(",")

    new_seat_taken = showtime.seat_taken + list_seat_id

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save()

            Booking.objects.filter(pk=booking.id).update(booking_total=total)
            Booking.objects.filter(pk=booking.id).update(seat_id=list_seat_id)
            Booking.objects.filter(pk=booking.id).update(seat_number=list_seat_label)
            Booking.objects.filter(pk=booking.id).update(showtime=showtime.id)

            Showtime.objects.filter(pk=showtime_id).update(seat_taken=new_seat_taken)

            return redirect(reverse('payment_success', args=[booking.booking_number]))
        else:
            messages.error(request, "There was an error with your form!")
    else:
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


def payment_success(request, booking_number):

    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f"Booking Successful! \
        Your booking number is {booking_number} \
            An email will be sent to {booking.email}.")

    if 'total' or 'seat_id' or 'seat_label' in request.session:
        del request.session['total']
        del request.session['seat_id']
        del request.session['seat_label']

    template = "booking/payment_success.html"

    context = {
        'booking': booking,
    }

    return render(request, template, context)
