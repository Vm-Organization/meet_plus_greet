from django import forms

from main_app.models import Account, Passenger


class AccountForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='Имя', required=False)
    last_name = forms.CharField(max_length=50, label='Фамилия', required=False)
    phone = forms.CharField(max_length=50, label='Телефон', required=False)
    personal_information = forms.CharField(max_length=50, label='Личная информация', required=False)
    organization = forms.CharField(max_length=50, label='Организация', required=False)

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'phone',
            'personal_information',
            'organization',
        ]


class PassengerForm(forms.ModelForm):
    last_name = forms.CharField(max_length=50, label='Фамилия')
    first_name = forms.CharField(max_length=50, label='Имя')
    middle_name = forms.CharField(max_length=50, label='Отчество', required=False)
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}, ))
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(max_length=50, label='Телефон', required=False)
    personal_information = forms.CharField(max_length=200, label='Личная информация', required=False)

    class Meta:
        model = Passenger
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'birth_date',
            'phone',
            'email',
            'personal_information',
        ]