from django.urls import path

from .views import AirportList, AirportDetail, AirportSearch


urlpatterns = [
    path('', AirportList.as_view(), name='airport_list'),
    path('<int:pk>/', AirportDetail.as_view(), name='airport_detail'),
    path('search/', AirportSearch.as_view(), name='airport_search'),
]
