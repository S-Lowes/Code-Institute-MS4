from django.shortcuts import render, get_object_or_404
from events.models import Showtime
# Create your views here.

def booking(request, showtime_id):
    """ A view to show the index page """

    showtime = get_object_or_404(Showtime, pk=showtime_id)
    seat_map = showtime.venue.seat_map
    seat_taken = showtime.seat_taken
    print(seat_taken)
    # Showtime.objects.filter(pk=showtime_id).update(seat_taken='8_2')

    if request.method == 'POST':
        data = request.POST
        print('data:')
        print(data)
        todo = data.get('payload')
        print('todo:')
        print(todo)

        x = todo.split(",")

        a = np.array(seat_taken)
        b = np.array(x)
        c = np.concatenate((a, b), axis=0)
        print(c)

        # taken_cookie = data.get()
        Showtime.objects.filter(pk=showtime_id).update(seat_taken=x)

    template = "booking/booking.html"

    context = {
        'showtime': showtime,
        'seat_map': seat_map,
        'seat_taken': seat_taken,

    }
    return render(request, template, context)
