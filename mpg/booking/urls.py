from django.urls import path

from .views import airport_booking_create, AirportAutocomplete, BookingView, TerminalAutocomplete, \
    terminal_booking_create, PassengerAutocomplete, passenger_booking_create, BookingDetailView, BookingListView

urlpatterns = [
    path('', BookingView.as_view(), name='booking_form'),
    path('airport/', airport_booking_create, name='airport_booking_create'),
    path('terminal/', terminal_booking_create, name='terminal_booking_create'),
    path('passenger/', passenger_booking_create, name='passenger_booking_create'),
    path('airport_autocomplete/', AirportAutocomplete.as_view(), name='airport_autocomplete'), # adding widget
    path('terminal_autocomplete/', TerminalAutocomplete.as_view(), name='terminal_autocomplete'),
    path('passenger_autocomplete/', PassengerAutocomplete.as_view(), name='passenger_autocomplete'),
    path('<int:pk>', BookingDetailView.as_view(), name='booking_detail'),
    path('list/', BookingListView.as_view(), name='booking_list'),
]
