from django import forms

from dal import autocomplete

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'departure_airport',
            # TODO add other fields
        ]

    widgets = {
        'departure_airport': autocomplete.ModelSelect2(url='airport_autocomplete'),
        # TODO add others
    }
