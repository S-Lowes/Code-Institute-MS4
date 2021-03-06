from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    date_start = models.DateField()
    date_end = models.DateField()
    run_time = models.IntegerField()
    description_short = models.TextField()
    description_long = models.TextField()
    image_hero = models.ImageField(null=True, blank=True)
    image_normal = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    capacity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    seat_map = ArrayField(models.CharField(
        max_length=254), default=list, null=True, blank=True)

    def __str__(self):
        return self.name


class Showtime(models.Model):
    event = models.ForeignKey(
        'Event', null=True, blank=True, on_delete=models.SET_NULL)
    venue = models.ForeignKey(
        'Venue', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    ticket_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    seat_taken = ArrayField(models.CharField(
        max_length=254), default=list, null=True, blank=True)

    def __str__(self):
        return self.event.name + ": " + str(
            self.date) + " at " + str(self.time)
