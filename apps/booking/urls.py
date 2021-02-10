from django.contrib import admin
from django.urls import path
from apps.booking.views import *


urlpatterns = [
    path('',booking, name='booking'),
    # path('clients/',views.ClientList, name='ClientList'),
    path('clients/',ClientsListView.as_view(), name='ClientList'),
]
