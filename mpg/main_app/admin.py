from django.contrib import admin
from .models import Account, Passenger, Service, ServicePrice

admin.site.register(Account)
admin.site.register(Passenger)
admin.site.register(Service)
admin.site.register(ServicePrice)
# Register your models here.
