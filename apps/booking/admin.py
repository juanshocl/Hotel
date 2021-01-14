from django.contrib import admin
from apps.booking.models import *

# Register your models here.
admin.site.register(Hotels)
admin.site.register(Booking)
admin.site.register(RoomsType)
admin.site.register(Features)
admin.site.register(Rooms)
admin.site.register(Category)
admin.site.register(PaymentMethod)
admin.site.register(Client)
admin.site.register(Payment)

