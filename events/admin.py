from django.contrib import admin
from .models import Event, Showtime, Venue, Price


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_start',
        'date_end',
        'run_time',
        'description_short',
        'description_long',
        'image_hero',
        'image_normal',
    )


class Venueadmin(admin.ModelAdmin):
    list_display = (
        'name',
        'capacity',
        'description',
        'image',
        'seat_map',
    )


class ShowtimeAdmin(admin.ModelAdmin):
    list_display = (
        'event',
        'venue',
        'date',
        'time',
    )


class Priceadmin(admin.ModelAdmin):
    list_display = (
        'showtime',
        'name',
        'price',
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Showtime, ShowtimeAdmin)
admin.site.register(Venue, Venueadmin)
admin.site.register(Price, Priceadmin)
