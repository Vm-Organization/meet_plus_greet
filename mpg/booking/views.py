from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.utils.html import format_html

from dal import autocomplete
from django.views.generic import DetailView, ListView
from formtools.wizard.views import SessionWizardView

from airport.models import Airport, Terminal
from chat.telegram import send_message
from main_app.models import Passenger
from .forms import AirportBookingForm, FlightInfoBookingForm, PassengerInfoForm
from .models import Booking, PassengerBooking


# view for creating widget autocompleting and selecting airport in booking
class AirportAutocomplete(autocomplete.Select2QuerySetView):
    def get_result_label(self, result):
        return format_html('<span style="font-weight: bold;">{}</span><br>{}<br>{}',
                           result.country, result.city, result.name)

    def get_selected_result_label(self, item):
        return item.name

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

    return render(request, 'booking/airport_booking_page1.html', {'form': form})


# view for adding widget autocompleting and selecting terminal in booking form
def terminal_booking_create(request):
    if request.method == 'POST':
        form = FlightInfoBookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FlightInfoBookingForm()

    return render(request, 'booking/flight_info_booking_page2.html', {'form': form})


# view for adding widget autocompleting and selecting passenger in booking form
def passenger_booking_create(request):
    if request.method == 'POST':
        form = PassengerInfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PassengerInfoForm()

    return render(request, 'booking/passenger_info_booking_page3.html', {'form': form})


FORMS = [
    ('airport', AirportBookingForm),
    ('flight_info', FlightInfoBookingForm),
    ('passenger_info', PassengerInfoForm)
]

TEMPLATES = {
    'airport': 'booking/airport_booking_page1.html',
    'flight_info': 'booking/flight_info_booking_page2.html',
    'passenger_info': 'booking/passenger_info_booking_page3.html'
}


# form wizard view: 3 or more pages
class BookingView(LoginRequiredMixin, SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        form_data = {**form_data[0], **form_data[1], **form_data[2]}
        passengers = form_data.pop('passenger')
        # create booking
        booking = Booking.objects.create(**form_data, user=self.request.user)
        booking.save()
        # add passengers to booking
        for passenger in passengers:
            passenger_booking = PassengerBooking.objects.create(booking=booking, passenger=passenger)
            passenger_booking.save()
        # calculate passenger number and total price
        booking.passenger_number = booking.get_passenger_number()
        booking.total_price = booking.get_total_price()
        booking.save()
        return render(self.request, 'booking/booking_detail.html',
                      {'form_data': [form.cleaned_data for form in form_list],
                       'booking': booking
                       })


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking'


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'booking'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingActiveListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_active_list.html'
    context_object_name = 'booking'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user, booking_status='unpaid' or 'paid' or 'confirmed')


# views for changing booking status
@login_required
def booking_confirm(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.booking_status = 'confirmed'
    booking.save()
    try:
        send_message(str(booking))
    except:
        pass
    return render(request, 'booking/booking_confirm.html')


@login_required
def booking_cancel(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.booking_status = 'canceled'
    booking.save()
    try:
        send_message(str(booking))
    except:
        pass
    return render(request, 'booking/booking_cancel.html')


@login_required
def booking_pay(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.booking_status = 'paid'
    booking.save()
    try:
        send_message(str(booking))
    except:
        pass
    return render(request, 'booking/booking_pay.html')
