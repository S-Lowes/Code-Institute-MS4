import uuid

from django.db import models
from profiles.models import UserProfile


# Create your models here.
class Booking(models.Model):
    booking_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    booking_total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    seat_numbers = models.CharField(max_length=50, null=False, blank=False)

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.booking_number


# class Ticket(models.Model):
# def __str__(self):
# return self.name
