from django_filters import FilterSet, CharFilter
from django.db.models import Q

from .models import Airport


class AirportFilter(FilterSet):
    search = CharFilter(method='filter_search', label='Search')

    # filtering unique values
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Airport.objects.values('name', 'country', 'city').distinct()

    class Meta:
        model = Airport
        fields = []

    # defining fields for searching
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(country__icontains=value) |
            Q(city__icontains=value)
        )
