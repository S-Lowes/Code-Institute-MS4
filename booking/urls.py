from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:showtime_id>/', views.booking, name='booking'),
    path('payment/<int:showtime_id>/', views.payment, name='payment'),
    path('payment_success/<booking_number>/', views.payment_success, name='payment_success'),
    path('wh/', webhook, name='webhook'),
]
