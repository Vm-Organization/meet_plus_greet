from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.JSONField(blank=True, null=True)

    # example:
    # messages = {'admin': 'Hello', 'user': 'Hi'}
