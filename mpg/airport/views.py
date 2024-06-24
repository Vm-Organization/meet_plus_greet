from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.utils.html import format_html

from dal import autocomplete

from main_app.models import Service
from .models import Airport
from .filters import AirportFilter
from .forms import AirportSearchForm


# list of airports
class AirportList(ListView):
    model = Airport
    template_name = 'airport/airport_list.html'
    context_object_name = 'airport_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # list of countries' unique values
        context['countries'] = Airport.objects.values('country').distinct().order_by('country')
        # list of airports' unique names
        context['airports'] = Airport.objects.values('pk', 'name', 'country').distinct()
        return context


# view of one airport
class AirportDetail(DetailView):
    model = Airport
    template_name = 'airport/airport_detail.html'
    context_object_name = 'airport'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departure_price_one_passenger'] = (
            self.object.service_price.get(service_type='departure').price_one_passenger)
        context['departure_price_others_passengers'] = (
            self.object.service_price.get(service_type='departure').price_others_passengers)
        context['arrival_price_one_passenger'] = (
            self.object.service_price.get(service_type='arrival').price_one_passenger)
        context['arrival_price_others_passengers'] = (
            self.object.service_price.get(service_type='arrival').price_others_passengers)
        context['transit_price_one_passenger'] = (
            self.object.service_price.get(service_type='transit').price_one_passenger)
        context['transit_price_one_passenger'] = (
            self.object.service_price.get(service_type='transit').price_others_passengers)
        context['service'] = self.object.service_price.first().service.name
        return context


# search an airport
class AirportSearch(ListView):
    model = Airport
    template_name = 'airport/airport_search.html'
    context_object_name = 'airport_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AirportFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class AirportSearchAutocomplete(autocomplete.Select2QuerySetView):
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


def search_airport(request):
    form = AirportSearchForm(request.GET)

    if form.is_valid():
        form.save()
        print('form valid')
    return render(request, 'airport/airport_search.html', {'form': form})
