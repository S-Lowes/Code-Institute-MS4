from django.contrib import admin
from .models import Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):

    readonly_fields = ('booking_number', 'showtime', 'date', 'seat_number',
                       'seat_id', 'booking_total', 'stripe_pid')

    fields = ('booking_number', 'showtime', 'date', 'full_name', 'email',
              'phone_number', 'seat_number', 'seat_id', 'booking_total',
              'stripe_pid')

    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
