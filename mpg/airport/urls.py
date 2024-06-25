from django.urls import path

from .views import AirportList, AirportDetail, AirportSearch, AirportSearchAutocomplete, search_airport


urlpatterns = [
    path('', AirportList.as_view(), name='airport_list'),
    path('<int:pk>/', AirportDetail.as_view(), name='airport_detail'),
    path('search/',search_airport, name='airport_search'),
    path('airport_search_autocomplete/', AirportSearchAutocomplete.as_view(), name='airport_search_autocomplete'),
]
