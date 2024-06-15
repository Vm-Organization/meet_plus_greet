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
        widget=autocomplete.ModelSelect2(url='airport_autocomplete',
                                         attrs={
                                             'data-html': True,
                                             'data-placeholder': 'Найти',
                                         }),
        label='Аэропорт отправления'
    )
    arrival_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=autocomplete.ModelSelect2(url='airport_autocomplete',
                                         attrs={
                                             'data-html': True,
                                             'data-placeholder': 'Найти',
                                         }),
        label='Аэропорт прибытия'
    )
    transit_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=autocomplete.ModelSelect2(url='airport_autocomplete',
                                         attrs={
                                             'data-html': True,
                                             'data-placeholder': 'Добавить транзитный пункт',
                                         }),
        label='Аэропорт транзита', required=False
    )

    class Meta:
        model = Booking
        fields = [
            'departure_airport',
            'arrival_airport',
            'transit_airport',
        ]


# stage 2: flight information
class FlightInfoBookingForm(forms.ModelForm):
    departure_datetime = forms.DateTimeField(widget=forms.DateTimeInput(
            attrs={
                'placeholder': 'Дата и время отправления',
                'required': '',
                'class': 'flatpickr'
            }),
        label='Время отправления')

    arrival_datetime = forms.DateTimeField(widget=forms.DateTimeInput(
            attrs={
                'placeholder': 'Дата и время прибытия',
                'required': '',
                'class': 'flatpickr'
            }),
        label='Время прибытия')

    flight_number = forms.CharField(max_length=50,
                                    widget=forms.TextInput(attrs={'placeholder': 'Номер рейса'}),
                                    label='Номер рейса')

    departure_terminal = forms.ModelChoiceField(
        queryset=Terminal.objects.all(),
        widget=autocomplete.ModelSelect2(url='terminal_autocomplete', attrs={
            'data-placeholder': 'Терминал отправления'}),
        label='Терминал отправления',
        required=False
    )

    arrival_terminal = forms.ModelChoiceField(
        queryset=Terminal.objects.all(),
        widget=autocomplete.ModelSelect2(url='terminal_autocomplete', attrs={
            'data-placeholder': 'Терминал прибытия'}),
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


# stage 3: passengers' and additional information
class PassengerInfoForm(forms.ModelForm):
    # passenger_number = forms.IntegerField(min_value=1, label='Number of Passengers')
    passenger = forms.ModelMultipleChoiceField(
        queryset=Passenger.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='passenger_autocomplete', attrs={'multiple': True}),
        label='Пассажир',
        required=False
    )
    email = forms.EmailField(label='Email',
                             required=False,
                             widget=forms.EmailInput(attrs={'placeholder': 'avv@gmail.com'}))
    phone = forms.CharField(max_length=50,
                            label='Телефон',
                            required=False,
                            widget=forms.TextInput(attrs={'placeholder': '+79117117171'}))
    telegram = forms.CharField(max_length=50,
                               label='Telegram',
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Telegram: @artur126'}))
    additional_info = forms.CharField(max_length=200,
                                      label='Дополнительная информация',
                                      required=False,
                                      widget=forms.TextInput(attrs={'placeholder': 'Дополнительная информация'}))

    class Meta:
        model = Booking
        fields = [
            'additional_info',
            'email',
            'phone',
            'telegram'
        ]
