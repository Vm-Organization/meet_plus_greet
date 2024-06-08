from django.urls import path

from .views import booking_create, AirportAutocomplete


urlpatterns = [
    path('create/', booking_create, name='booking_create'),
    path('airport_autocomplete/', AirportAutocomplete.as_view(), name='airport_autocomplete'), # adding widget
]
