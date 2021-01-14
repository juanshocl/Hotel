from django.db import models
from apps.registration.models import UserProfile

import uuid

class Hotels(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, default=None)
    Rut = models.CharField(max_length=50, default=None)
    Address = models.CharField(max_length=50, default=None)
    Rooms = models.IntegerField
    Descriptions = models.CharField(max_length=50, default=None)
    UserId = models.ForeignKey('registration.UserProfile', on_delete=models.CASCADE, default=None)

class RoomsType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RoomsDescription = models.CharField(max_length=50, default = None)
    RoomsId = models.ForeignKey('Rooms', on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.RoomsDescription


class Features(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    Element = models.CharField(max_length=50, default=None)
    Quantity = models.IntegerField
    RoomsId = models.ForeignKey('Rooms', on_delete=models.CASCADE, default = None)

    
class Rooms(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    HotelId = models.ForeignKey('Hotels', on_delete=models.CASCADE, default=None)
    RoomsCapacity = models.IntegerField
    RoomsName = models.CharField(max_length=50, default=None)
    RoomsPrice = models.IntegerField
    RoomsIs_active = models.BooleanField
    RoomsTypeId = models.ManyToManyField(RoomsType)
    FeaturesId = models.ForeignKey('Features', on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.RoomsName



class Category(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CategoryDescription = models.CharField(max_length=50, default = None)

    def __str__(self):
        return self.CategoryDescription

class PaymentMethod(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PaymentMethodDescription = models.CharField(max_length=50, default = None)
    
    def __str__(self):
        return PaymentMethodDescription

class Client(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, default = None)
    LastName = models.CharField(max_length=50, default = None)
    Rut = models.CharField(max_length=50, default = None)
    Address = models.CharField(max_length=50, default = None)
    Phone = models.CharField(max_length=50, default = None)
    Email = models.CharField(max_length=50, default = None)
    Nationality = models.CharField(max_length=50, default = None)
    #BookingId = models.ForeignKey('Booking', on_delete=models.CASCADE, default=None) 



class Payment(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    IdHotel = models.ForeignKey('registration.UserProfile', on_delete=models.CASCADE, default=None)
    Mount = models.IntegerField
    IdBook = models.ForeignKey('Booking', on_delete=models.CASCADE, default=None)
    Date = models.DateTimeField(auto_now_add=True)
    PaymentMethodId = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, default=None)

    def __str__(self):
        pass

    class Meta:
        db_table = 'Payment'
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


class Booking(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DateCheckIn = models.DateField(default=None)
    TimeCheckIn = models.TimeField(default=None)
    DateCheckOut = models.DateField(default=None)
    TimeCheckOut = models.TimeField(default=None)
    #test = models.CharField(max_length = 50, default=None)
    Prepaid = models.BooleanField
    AubscriberMount = models.IntegerField
    #PaymentId = models.ForeignKey('Payment', on_delete=models.CASCADE, default=None)
    Is_Active = models.BooleanField
    #ClientId = models.ForeignKey('Client', on_delete=models.CASCADE, default=None) 
