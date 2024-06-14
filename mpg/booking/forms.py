from django import forms

from dal import autocomplete
from formset.widgets import DateTimeInput

from .models import Booking


# stage 1: departure, arrival, transit: additional
class AirportBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'departure_airport',
            'arrival_airport',
            'transit_airport',
        ]

        widgets = {
            'departure_airport': autocomplete.ModelSelect2(url='airport_autocomplete',
                                                           attrs={'data-html': True,
                                                                  'data-placeholder': 'Найти'}),
            'arrival_airport': autocomplete.ModelSelect2(url='airport_autocomplete',
                                                         attrs={'data-html': True,
                                                                'data-placeholder': 'Найти'}),
            'transit_airport': autocomplete.ModelSelect2(url='airport_autocomplete',
                                                         attrs={'data-html': True,
                                                                'data-placeholder': 'Добавить транзитный пункт'}),
        }


# stage 2: flight information
class FlightInfoBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'departure_terminal',
            'arrival_terminal',
            'flight_number',
            'departure_datetime',
            'arrival_datetime',
        ]

        widgets = {
            'departure_terminal': autocomplete.ModelSelect2(url='terminal_autocomplete'),
            'arrival_terminal': autocomplete.ModelSelect2(url='terminal_autocomplete'),
            'departure_datetime': DateTimeInput,
            'arrival_datetime': DateTimeInput,
        }


# stage 3: passengers' and additional information
class PassengerInfoForm(forms.ModelForm):
    passenger_number = forms.IntegerField(min_value=1, label='Number of Passengers')
    
    class Meta:
        model = Booking
        fields = [
            'passenger',
            'additional_info',
            'email',
            'phone',
            'telegram'
        ]

        widgets = {
            'passenger': autocomplete.ModelSelect2Multiple(url='passenger_autocomplete'),
        }
