import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from events.models import Showtime
from profiles.models import UserProfile


# Create your models here.
class Booking(models.Model):
    booking_number = models.CharField(max_length=32,
                                      null=False, editable=False)
    showtime = models.ForeignKey(Showtime, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='booking')

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    seat_number = ArrayField(models.CharField(max_length=254,
                                              blank=True), default=list)
    seat_id = ArrayField(models.CharField(max_length=254,
                                          blank=True), default=list)
    booking_total = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking number
        if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number
