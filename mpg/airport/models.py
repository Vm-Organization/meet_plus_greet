from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)


class Terminal(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    name = models.CharField()
