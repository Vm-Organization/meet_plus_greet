from django.shortcuts import render, redirect

from dal import autocomplete

from airport.models import Airport
from .models import Booking
from .forms import BookingForm


# view for autocompleting and selecting airport in booking
class AirportAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Airport.objects.values('name').distinct()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()

    return render(request, 'booking/booking_form.html', {'form': form})
