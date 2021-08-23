from django.shortcuts import render


# Create your views here.
def booking(request):
    """ A view to show the booking page """

    return render(request, 'booking/booking.html')
