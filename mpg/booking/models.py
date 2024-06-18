from django.db import models
from django.contrib.auth.models import User

from airport.models import Airport, Terminal
from main_app.models import ServicePrice, Passenger
from main_app.utils import valid_phone_number


class Booking(models.Model):
    BOOKING_STATUS = [
        ('unpaid', 'Не оплачен'),
        ('paid', 'Оплачен'),
        ('confirmed', 'Подтвержден'),
        ('cancelled', 'Отменен'),
        ('completed', 'Завершен'),
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
    passenger_number = models.PositiveIntegerField(default=1)
    passenger = models.ManyToManyField(Passenger, through='PassengerBooking')

    additional_info = models.TextField(blank=True, null=True)

    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True, validators=[valid_phone_number])
    telegram = models.CharField(max_length=100, blank=True, null=True)

    total_price = models.CharField(max_length=50, null=True)  # TODO: function to calculate total price

    date_created = models.DateTimeField(auto_now_add=True)

    def get_passenger_number(self):
        """Using after saving, in view"""
        return PassengerBooking.objects.filter(booking=self).count()

    def get_total_price(self):
        """Using after saving, in view"""
        # if no passenger we will count for one passenger
        passenger_number = self.get_passenger_number() or self.passenger_number
        try:
            departure_service_one = float(ServicePrice.objects.get(
                airport=self.departure_airport,
                service_type='departure').price_one_passenger)
            departure_service_others = float(ServicePrice.objects.get(
                airport=self.departure_airport,
                service_type='departure').price_others_passengers)
            arrival_service_one = float(ServicePrice.objects.get(
                airport=self.arrival_airport,
                service_type='arrival').price_one_passenger)
            arrival_service_others = float(ServicePrice.objects.get(
                airport=self.arrival_airport,
                service_type='arrival').price_others_passengers)
            if self.transit_airport:
                transit_service_one = float(ServicePrice.objects.get(
                    airport=self.transit_airport,
                    service_type='transit').price_one_passenger)
                transit_service_others = float(ServicePrice.objects.get(
                    airport=self.transit_airport,
                    service_type='transit').price_others_passengers)
            else:
                transit_service_one = 0
                transit_service_others = 0
            total = (departure_service_one + arrival_service_one + transit_service_one +
                     (departure_service_others + arrival_service_others + transit_service_others) *
                     (passenger_number - 1))
        except ValueError:
            total = "By request"
        return total

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.phone:
            self.phone = valid_phone_number(self.phone)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.pk), self.booking_status


class PassengerBooking(models.Model):
    """Connection between booking and passenger"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='passenger_booking')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='passenger_booking')
