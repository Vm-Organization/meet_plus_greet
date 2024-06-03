from django.db import models
from django.contrib.auth.models import User

from airport.models import Airport, Terminal
from main_app.models import ServicePrice


class Booking(models.Model):
    PASSENGER_AGE = [
        ('infant', 'Ребенок (0-2 лет)'),
        ('child', 'Ребенок (2-12 лет)'),
        ('adult', 'Взрослый'),
    ]

    BOOKING_STATUS = [
        ('unpaid', 'Не оплачен'),
        ('paid', 'Оплачен'),
        ('confirmed', 'Подтвержден'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')

    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_booking')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_booking')

    departure_terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='departure_booking')
    arrival_terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='arrival_booking')

    departure_service = models.ForeignKey(ServicePrice, on_delete=models.CASCADE, related_name='departure_service')
    arrival_service = models.ForeignKey(ServicePrice, on_delete=models.CASCADE, related_name='arrival_service')

    flight_number = models.CharField(max_length=100)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()

    booking_status = models.CharField(max_length=100, choices=BOOKING_STATUS)

    passenger_age = models.CharField(max_length=100, choices=PASSENGER_AGE)
    passenger_number = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
