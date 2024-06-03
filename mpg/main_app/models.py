from django.contrib.auth.models import User
from django.db import models

from airport.models import Airport


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ServicePrice(models.Model):
    """Connection between service and price"""
    SERVICE_TYPE = [
        ('arrival', 'Прилет'),
        ('departure', 'Вылет'),
        ('transit', 'Транзит'),
    ]

    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='service_price')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_price')

    service_type = models.CharField(max_length=100, choices=SERVICE_TYPE)
    price_one_passenger = models.CharField(max_length=50)
    price_others_passengers = models.CharField(max_length=50)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    personal_information = models.TextField(blank=True, null=True)
    booking_history = models.TextField(blank=True, null=True)
    profile_configuration = models.JSONField(blank=True, null=True)
    organization = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


class Passenger(models.Model):
    PASSENGER_AGE = [
        ('infant', 'Ребенок (0-2 лет)'),
        ('child', 'Ребенок (2-12 лет)'),
        ('adult', 'Взрослый'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100, choices=PASSENGER_AGE)
    # for documents. need to be hashed in future for security:
    personal_data = models.CharField(max_length=500, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
