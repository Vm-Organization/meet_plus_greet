from django import forms

from dal import autocomplete

from .models import Airport


class AirportSearchForm(forms.ModelForm):
    search = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=autocomplete.ModelSelect2(url='airport_search_autocomplete',
                                         attrs={
                                             'data-html': True,
                                             'data-placeholder': 'Город, аэропорт или терминал...',
                                         }),
        label='Search'
    )

    class Meta:
        model = Airport
        fields = ('__all__')