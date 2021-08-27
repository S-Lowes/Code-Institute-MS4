from django import forms
# from .widgets import CustomClearableFileInput
from .models import Event, Venue, Showtime


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    # image_hero = forms.ImageField(label='Hero Image', required=False, widget=CustomClearableFileInput)
    # image_normal = forms.ImageField(label='Normal Image', required=False, widget=CustomClearableFileInput)


class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = '__all__'

    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


class ShowtimeForm(forms.ModelForm):

    class Meta:
        model = Showtime
        fields = '__all__'
        exclude = ['seat_taken']
