from django.urls import path
from . import views


urlpatterns = [
    path('<int:showtime_id>/', views.booking, name='booking'),
]
