from django import forms

from dal import autocomplete
from django.http import request
from formset.widgets import DateTimeInput

from airport.models import Airport, Terminal
from main_app.models import Passenger
from .models import Booking, PassengerBooking


# stage 1: departure, arrival, transit: additional
class AirportBookingForm(forms.ModelForm):
    departure_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=autocomplete.ModelSelect2(url='airport_autocomplete'),
        label='Аэропорт отправления'
    )
    arrival_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=autocomplete.ModelSelect2(url='airport_autocomplete'),
        label='Аэропорт прибытия'
    )
    transit_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=autocomplete.ModelSelect2(url='airport_autocomplete'),
        label='Аэропорт транзита', required=False
    )

    class Meta:
        model = Booking
        fields = [
            'departure_airport',
            'arrival_airport',
            'transit_airport',
        ]

        # widgets = {
        #     'departure_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
        #     'arrival_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
        #     'transit_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
        # }


# stage 2: flight information
class FlightInfoBookingForm(forms.ModelForm):
    departure_datetime = forms.DateTimeField(widget=DateTimeInput, label='Время отправления')
    arrival_datetime = forms.DateTimeField(widget=DateTimeInput, label='Время прибытия')
    flight_number = forms.CharField(max_length=50, label='Номер рейса')
    departure_terminal = forms.ModelChoiceField(
        queryset=Terminal.objects.all(),
        widget=autocomplete.ModelSelect2(url='terminal_autocomplete'),
        label='Терминал отправления',
        required=False
    )
    arrival_terminal = forms.ModelChoiceField(
        queryset=Terminal.objects.all(),
        widget=autocomplete.ModelSelect2(url='terminal_autocomplete'),
        label='Терминал прибытия',
        required=False
    )

    class Meta:
        model = Booking
        fields = [
            'departure_terminal',
            'arrival_terminal',
            'flight_number',
            'departure_datetime',
            'arrival_datetime',
        ]

        # widgets = {
        #     'departure_terminal': autocomplete.ModelSelect2(url='terminal_autocomplete'),
        #     'arrival_terminal': autocomplete.ModelSelect2(url='terminal_autocomplete'),
        #     'departure_datetime': DateTimeInput,
        #     'arrival_datetime': DateTimeInput,
        # }


# stage 3: passengers' and additional information
class PassengerInfoForm(forms.ModelForm):
    # passenger_number = forms.IntegerField(min_value=1, label='Number of Passengers')
    passenger = forms.ModelMultipleChoiceField(
        queryset=Passenger.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='passenger_autocomplete', attrs={'multiple': True}),
        label='Пассажир',
        required=False
    )
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(max_length=50, label='Телефон', required=False)
    telegram = forms.CharField(max_length=50, label='Telegram', required=False)
    additional_info = forms.CharField(max_length=200, label='Дополнительная информация', required=False)
    
    class Meta:
        model = Booking
        fields = [
            # 'passenger_number',
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


# class PassengerBookingForm(forms.Form):
#     passanger = forms.ModelChoiceField(queryset=Passenger.objects.all(),
#                                        widget=autocomplete.ModelSelect2(url='passenger_autocomplete'))
#
#     class Meta:
#         model = PassengerBooking
#         fields = '__all__'