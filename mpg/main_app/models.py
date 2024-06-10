from django.contrib.auth.models import User
from django.db import models

from airport.models import Airport
from main_app.utils import valid_phone_number, age_type


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
    price_one_passenger = models.CharField(max_length=100)
    price_others_passengers = models.CharField(max_length=100)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, validators=[valid_phone_number])
    personal_information = models.TextField(blank=True, null=True)
    profile_configuration = models.JSONField(blank=True, null=True)
    organization = models.CharField(max_length=150, blank=True, null=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.phone = valid_phone_number(self.phone)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.user}"


class Passenger(models.Model):
    """Here should be added hashing for safety"""
    PASSENGER_AGE = [
        ('infant', 'Ребенок (0-2 лет)'),
        ('child', 'Ребенок (2-12 лет)'),
        ('adult', 'Взрослый'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(validators=[age_type])
    age = models.CharField(max_length=100, choices=PASSENGER_AGE)
    phone = models.CharField(max_length=20, blank=True, null=True, validators=[valid_phone_number])
    email = models.EmailField(blank=True, null=True)
    personal_data = models.CharField(max_length=500, blank=True, null=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.phone = valid_phone_number(self.phone)
        # self.age = age_type(self.birth_date)[0]  # for english
        self.age = age_type(self.birth_date)[1]  # for russian
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
