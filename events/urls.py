from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_showtimes, name='showtimes'),
    path('event-management/', views.event_management, name='event_management'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-venue/', views.add_venue, name='add_venue'),
    path('add-showtime/', views.add_showtime, name='add_showtime'),
    path('edit-event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('edit-venue/<int:venue_id>/', views.edit_venue, name='edit_venue'),
    path('edit-showtime/<int:showtime_id>/', views.edit_showtime, name='edit_showtime'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('delete-venue/<int:venue_id>/', views.delete_venue, name='delete_venue'),
    path('delete/<int:showtime_id>/', views.delete_showtime, name='delete_showtime'),
]
