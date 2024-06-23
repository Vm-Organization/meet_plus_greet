from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    UpdateView,
    FormView,
    DetailView,
    CreateView,
    ListView,
    DeleteView
)

from main_app.forms import AccountForm, PassengerForm
from main_app.models import Account, Passenger


def home(request):
    return TemplateView.as_view(template_name='main/home.html')


class HomeView(TemplateView):
    template_name = 'main/home.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


class ReviewsView(TemplateView):
    template_name = 'main/reviews.html'


class AccountView(LoginRequiredMixin, TemplateView):
    model = Account
    fields = '__all__'
    template_name = 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'], created = self.model.objects.get_or_create(user=self.request.user)
        return context


class AccountEditView(LoginRequiredMixin, UpdateView):
    form_class = AccountForm
    model = Account
    template_name = 'account/account_edit.html'

    def get_object(self, queryset=None):
        object, created = self.model.objects.get_or_create(user=self.request.user)
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.model.objects.get(user=self.request.user)
        context['form'] = self.form_class(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('account')


class PassengerDetailView(LoginRequiredMixin, DetailView):
    """Here should be added some permissions for safety"""
    model = Passenger
    template_name = 'passenger/passenger.html'
    context_object_name = 'passenger'
    form = PassengerForm


class PassengerCreateView(LoginRequiredMixin, CreateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passenger/passenger_create.html'

    def form_valid(self, form):
        passenger = form.save(commit=False)
        passenger.user = self.request.user
        passenger.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account')


class PassengerEditView(LoginRequiredMixin, UpdateView):
    """Birth_date not supplied but should be"""  # TODO
    model = Passenger
    form_class = PassengerForm
    context_object_name = 'passenger'
    template_name = 'passenger/passenger_edit.html'

    def get_success_url(self):
        return reverse('account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(self.get_success_url())


class PassengerListView(LoginRequiredMixin, ListView):
    model = Passenger
    ordering = ['last_name']
    template_name = 'passenger/passenger_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passengers'] = self.model.objects.filter(user=self.request.user)
        return context


class PassengerDeleteView(LoginRequiredMixin, DeleteView):
    model = Passenger
    template_name = 'passenger/passenger_delete.html'
    success_url = reverse_lazy('account')
    context_object_name = 'passenger'
