from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_showtimes, name='showtimes'),
    path('event-management/', views.event_management, name='event_management'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-venue/', views.add_venue, name='add_venue'),
    path('add-showtime/', views.add_showtime, name='add_showtime'),
]
