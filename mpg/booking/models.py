from django.db import models
from django.contrib.auth.models import User

from airport.models import Airport, Terminal
from main_app.models import ServicePrice, Passenger


class Booking(models.Model):
    BOOKING_STATUS = [
        ('unpaid', 'Не оплачен'),
        ('paid', 'Оплачен'),
        ('confirmed', 'Подтвержден'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')

    booking_status = models.CharField(max_length=100, choices=BOOKING_STATUS, default='unpaid')

    # stage 1 fields
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_booking')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_booking')
    transit_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='transit_booking', blank=True,
                                        null=True)

    # stage 2 fields
    departure_terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='departure_booking',
                                           default=14)
    arrival_terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='arrival_booking',
                                         default=14)

    flight_number = models.CharField(max_length=100)

    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()

    # stage 3 fields
    passenger_number = models.PositiveIntegerField()
    passenger = models.ManyToManyField(Passenger, through='PassengerBooking')

    additional_info = models.TextField(blank=True, null=True)

    email = models.EmailField()
    phone = models.CharField(max_length=15)
    telegram = models.CharField(max_length=100, blank=True, null=True)

    total_price = models.CharField(max_length=50, null=True)  # TODO: function to calculate total price

    # off-stage: for determining prices
    departure_service = models.ForeignKey(ServicePrice, on_delete=models.CASCADE, related_name='departure_service',
                                          blank=True, null=True)
    arrival_service = models.ForeignKey(ServicePrice, on_delete=models.CASCADE, related_name='arrival_service',
                                        blank=True, null=True)
    transit_service = models.ForeignKey(ServicePrice, on_delete=models.CASCADE, related_name='transit_service',
                                        blank=True, null=True)

    def __str__(self):
        return self.pk


class PassengerBooking(models.Model):
    """Connection between booking and passenger"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='passenger_booking')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='passenger_booking')
    date_created = models.DateTimeField(auto_now_add=True)
