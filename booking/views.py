from django.shortcuts import render, redirect, reverse, \
    get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import Booking
from .forms import BookingForm
from events.models import Showtime
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.contrib.auth.decorators import login_required

import stripe
# Create your views here.


@login_required
def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)

    seat_map = showtime.venue.seat_map
    seat_taken = showtime.seat_taken
    ticket_price = showtime.ticket_price

    # AJAX Request
    if request.method == 'POST':
        data = request.POST
        total = data.get('total_recalc')
        seat_id = data.get('id_recalc')
        seat_label = data.get('label_recalc')

        request.session['total'] = total
        request.session['seat_id'] = seat_id
        request.session['seat_label'] = seat_label
        request.session['showtime_id'] = showtime.id

        return JsonResponse({'status': 'Data Acquired By View!'})

    template = "booking/booking.html"

    context = {
        'showtime': showtime,
        'seat_map': seat_map,
        'seat_taken': seat_taken,
        'ticket_price': ticket_price,

    }
    return render(request, template, context)


@require_POST
def cache_user_booking_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'total': request.session['total'],
            'seat_id': request.session['seat_id'],
            'seat_label': request.session['seat_label'],
            'showtime_id': request.session['showtime_id'],
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def payment(request, showtime_id):

    booking_form = BookingForm()
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    total = request.session['total']
    seat_id = request.session['seat_id']
    seat_label = request.session['seat_label']

    list_seat_id = seat_id.lstrip("[").rstrip("]").replace('"', '').split(",")
    list_seat_label = seat_label.lstrip(
        "[").rstrip("]").replace('"', '').split(",")

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
            booking = booking_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            booking.stripe_pid = pid
            booking.booking_total = total
            booking.seat_id = list_seat_id
            booking.seat_number = list_seat_label
            booking.save()

            Showtime.objects.filter(pk=showtime_id).update(
                seat_taken=new_seat_taken)
            Booking.objects.filter(pk=booking.id).update(showtime=showtime.id)

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success', args=[
                booking.booking_number]))
        else:
            messages.error(request, "There was an error with your form!")
    else:
        stripe_total = round(int(total)*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            booking_form = BookingForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                })
        except UserProfile.DoesNotExist:
            booking_form = BookingForm()
    else:
        booking_form = BookingForm()

    template = "booking/payment.html"

    context = {
        'booking_form': booking_form,
        'showtime': showtime,
        'total': total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


@login_required
def payment_success(request, booking_number):

    save_info = request.session.get('save_info')
    print(save_info)
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f"Booking Successful! \
        Your booking number is {booking_number} ")

    profile = UserProfile.objects.get(user=request.user)
    booking.user_profile = profile
    booking.save()

    if save_info:
        profile_data = {
            'default_phone_number': booking.phone_number
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    if 'total' or 'seat_id' or 'seat_label' in request.session:
        del request.session['total']
        del request.session['seat_id']
        del request.session['seat_label']

    template = "booking/payment_success.html"

    context = {
        'booking': booking,
    }

    return render(request, template, context)
