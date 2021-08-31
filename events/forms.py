from django import forms
from .models import Event, Venue, Showtime


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'



class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = '__all__'



class ShowtimeForm(forms.ModelForm):

    class Meta:
        model = Showtime
        fields = '__all__'
        exclude = ['seat_taken']
