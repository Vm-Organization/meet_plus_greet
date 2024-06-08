from django.urls import path

from main_app.views import (AccountView,
                            AccountEditView,
                            PassengerDetailView,
                            PassengerCreateView,
                            PassengerEditView,
                            PassengerListView,
                            PassengerDeleteView, home, HomeView
                            )

urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('account/edit/', AccountEditView.as_view(), name='account_edit'),

    path('passenger/<int:pk>/', PassengerDetailView.as_view(), name='passenger_detail'),
    path('passenger/create/', PassengerCreateView.as_view(), name='passenger_create'),
    path('passenger/<int:pk>/edit/', PassengerEditView.as_view(), name='passenger_edit'),
    path('passenger/list/', PassengerListView.as_view(), name='passenger_list'),
    path('passenger/<int:pk>/delete/', PassengerDeleteView.as_view(), name='passenger_delete'),

    path('', HomeView.as_view(), name='home'),
    ]