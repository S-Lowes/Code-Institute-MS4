from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Booking, Showtime
from profiles.models import UserProfile

import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id

        total = intent.metadata.total
        seat_id = intent.metadata.seat_id
        seat_label = intent.metadata.seat_label
        showtime_id = intent.metadata.showtime_id
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = billing_details.phone
                profile.save()

        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    stripe_pid=pid,
                )
                booking_exists = True
                break
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if booking_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            booking = None
            try:
                booking = Booking.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    stripe_pid=pid,
                )

                list_seat_id = seat_id.lstrip("[").rstrip("]").replace('"', '').split(",")
                list_seat_label = seat_label.lstrip("[").rstrip("]").replace('"', '').split(",")

                showtime = get_object_or_404(Showtime, pk=showtime_id)
                old_seat_taken = showtime.seat_taken
                new_seat_taken = old_seat_taken + list_seat_id

                Booking.objects.filter(pk=booking.id).update(booking_total=total)
                Booking.objects.filter(pk=booking.id).update(seat_id=list_seat_id)
                Booking.objects.filter(pk=booking.id).update(seat_number=list_seat_label)
                Booking.objects.filter(pk=booking.id).update(showtime=showtime_id)

                Showtime.objects.filter(pk=showtime_id).update(seat_taken=new_seat_taken)

            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Error: {e}' ,
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
