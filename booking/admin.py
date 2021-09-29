from django.contrib import admin
from .models import Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):

    readonly_fields = ('booking_number', 'showtime', 'date', 'seat_number',
                       'seat_id', 'booking_total', 'stripe_pid')

    fields = ('booking_number', 'user_profile', 'showtime', 'date',
              'full_name', 'email', 'phone_number', 'seat_number',
              'seat_id', 'booking_total', 'stripe_pid')

    list_display = ('booking_number', 'date', 'user_profile', 'full_name',
                    'booking_total', 'seat_number', 'seat_id',)

    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
