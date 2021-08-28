from django.urls import path
from . import views


urlpatterns = [
    path('<int:showtime_id>/', views.booking, name='booking'),
    path('<int:showtime_id>/', views.payment, name='payment'),
]
