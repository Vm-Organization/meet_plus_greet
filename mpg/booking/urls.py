from django.urls import path

from .views import airport_booking_create, AirportAutocomplete, BookingView, TerminalAutocomplete, terminal_booing_create

urlpatterns = [
    path('', BookingView.as_view(), name='booking_form'),
    path('create/', airport_booking_create, name='airport_booking_create'),
    path('book', terminal_booing_create, name='terminal_booking_create'),
    path('airport_autocomplete/', AirportAutocomplete.as_view(), name='airport_autocomplete'), # adding widget
    path('terminal_autocomplete/', TerminalAutocomplete.as_view(), name='terminal_autocomplete'),
]
