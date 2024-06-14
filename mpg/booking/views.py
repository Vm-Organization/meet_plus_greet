from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from dal import autocomplete
from django.views.generic import DetailView, ListView
from formtools.wizard.views import SessionWizardView

from airport.models import Airport, Terminal
from main_app.models import Passenger
from .forms import AirportBookingForm, FlightInfoBookingForm, PassengerInfoForm, BookingDetailForm
from .models import Booking, PassengerBooking


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
class BookingView(LoginRequiredMixin, SessionWizardView):
    form_list = [AirportBookingForm, FlightInfoBookingForm, PassengerInfoForm]
    template_name = 'booking/booking_wizard_form.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        form_data = {**form_data[0], **form_data[1], **form_data[2]}
        passengers = form_data.pop('passenger')
        booking = Booking.objects.create(**form_data, user=self.request.user)
        booking.save()
        for passenger in passengers:
            passenger_booking = PassengerBooking.objects.create(booking=booking, passenger=passenger)
            passenger_booking.save()
        booking.passenger_number = booking.get_passenger_number()
        booking.total_price = booking.get_total_price()
        booking.save()
        return render(self.request, 'booking/booking_detail.html',
                      {'form_data': [form.cleaned_data for form in form_list],
                       'booking': booking
                       })


class BookingDetailView(LoginRequiredMixin, DetailView):
    form_class = BookingDetailForm
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking'


class BookingListView(LoginRequiredMixin, ListView):
    form = BookingDetailForm
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'booking'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


def booking_confirm(request):
    pass
    # return render(request, 'booking/booking_complete.html')


def booking_cancel(request):
    pass
    # return render(request, 'booking/booking_cancel.html')


def booking_pay(request):
    pass
    # return render(request, 'booking/booking_pay.html')
