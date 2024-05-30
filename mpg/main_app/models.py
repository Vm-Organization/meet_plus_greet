from django.db import models

from airport.models import Airport


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class ServicePrice(models.Model):
    SERVICE_TYPE = [
        ('arrival', 'Прилет'),
        ('departure', 'Вылет'),
        ('transit', 'Транзит'),
    ]

    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='service_price')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_price')

    service_type = models.CharField(max_length=100, choices=SERVICE_TYPE)
    price_one_passenger = models.FloatField(blank=True, null=True)
    price_others_passengers = models.FloatField(blank=True, null=True)
