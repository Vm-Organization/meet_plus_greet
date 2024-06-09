from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code}, {self.name}, {self.city}, {self.country}"


class Terminal(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
