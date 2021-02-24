from django.contrib import admin
from django.urls import path
from apps.booking.views import *


urlpatterns = [
    path('',bookingHome.as_view(), name='bookingHome'),
    # path('clients/',views.ClientList, name='ClientList'),
    path('clientslist/',ClientsListView.as_view(), name='ClientList'),
    path('addclients/',ClientsCreateView.as_view(), name='ClientCreate'),
    path('addbooking/',BookingCreateView.as_view(), name='BookingCreate'),
    path('addpayment/',PaymentCreateView.as_view(), name='paymentCreate'),
    path('addpaymentmethod/',PaymentmethodCreateView.as_view(), name='paymentmethodCreate'),
    path('addrooms/',RoomsCreateView.as_view(), name='roomsCreate'),
    path('addfeature/',FeatureCreateView.as_view(), name='featureCreate'),
    path('addroomstype/',RoomstypeCreateView.as_view(), name='roomstypeCreate'),
    path('addhotel/',HotelCreateView.as_view(), name='hotelCreate'),
    path('calendar/',Calendar.as_view(), name='Calendar'),
    

]
