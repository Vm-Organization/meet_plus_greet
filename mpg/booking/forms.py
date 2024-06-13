from django import forms

from dal import autocomplete
from formset.widgets import DateTimeInput

from main_app.models import Passenger
from .models import Booking, PassengerBooking


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
            'departure_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
            'arrival_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
            'transit_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
        }


# stage 2: flight information
class FlightInfoBookingForm(forms.ModelForm):
    departure_datetime = forms.DateTimeField(widget=DateTimeInput)
    arrival_datetime = forms.DateTimeField(widget=DateTimeInput)

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
    # passanger = forms.ModelChoiceField(queryset=Passenger.objects.all(), widget=autocomplete.ModelSelect2(url='passenger_autocomplete'), required=False)
    
    class Meta:
        model = Booking
        fields = [
            'passenger_number',
            # 'passenger',
            'additional_info',
            'email',
            'phone',
            'telegram'
        ]

        # widgets = {
        #     'passenger': autocomplete.ModelSelect2Multiple(url='passenger_autocomplete'),
        # }


class BookingDetailForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class PassengerBookingForm(forms.Form):
    passanger = forms.ModelChoiceField(queryset=Passenger.objects.all(),
                                       widget=autocomplete.ModelSelect2(url='passenger_autocomplete'))

    class Meta:
        model = PassengerBooking
        fields = '__all__'