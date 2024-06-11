from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from dal import autocomplete
from formtools.wizard.views import SessionWizardView

from airport.models import Airport, Terminal
from main_app.models import Passenger
from .forms import AirportBookingForm, FlightInfoBookingForm, PassengerInfoForm


# TODO: add is_authenticated in autocomplete widget + add LoginRequired for forms
# TODO: if 2 passengers, there are more passenger forms for them
# view for creating widget autocompleting and selecting airport in booking
class AirportAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Airport.objects.all()

        if self.q:
            qs = qs.filter(
                Q(name__icontains=self.q) |
                Q(country__icontains=self.q) |
                Q(city__icontains=self.q)
            )

        return qs


# view for creating widget autocompleting and selecting terminal in booking
class TerminalAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Terminal.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


# view for creating widget autocompleting and selecting passenger in booking
class PassengerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        user = self.request.user
        qs = Passenger.objects.filter(user=user)

        if self.q:
            qs = qs.filter(
                Q(last_name__icontains=self.q) |
                Q(first_name__icontains=self.q)
            )

        return qs


# view for adding widget autocompleting and selecting airport in booking form
def airport_booking_create(request):
    if request.method == 'POST':
        form = AirportBookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AirportBookingForm()

    return render(request, 'booking_wizard_form.html', {'form': form})


# view for adding widget autocompleting and selecting terminal in booking form
def terminal_booking_create(request):
    if request.method == 'POST':
        form = FlightInfoBookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FlightInfoBookingForm()

    return render(request, 'booking_wizard_form.html', {'form': form})


# view for adding widget autocompleting and selecting passenger in booking form
def passenger_booking_create(request):
    if request.method == 'POST':
        form = PassengerInfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PassengerInfoForm()

    return render(request, 'booking_wizard_form.html', {'form': form})


# form wizard view: 3 or more pages
class BookingView(SessionWizardView):
    form_list = [AirportBookingForm, FlightInfoBookingForm, PassengerInfoForm]
    template_name = 'booking/booking_wizard_form.html'

    def done(self, form_list, **kwargs):
        return HttpResponse('Form submitted')
