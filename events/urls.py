from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_showtimes, name='showtimes'),
    path('add/', views.add_event, name='add_event'),
]
