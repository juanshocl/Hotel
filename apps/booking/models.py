from django.db import models
from datetime import datetime,date,timedelta
from apps.registration.models import UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save

import uuid

class Hotels(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50,verbose_name="Nombre Hotel", default=None)
    Rut = models.CharField(max_length=50, verbose_name="Rut Empresa", default=None)
    Address = models.CharField(max_length=50, verbose_name="Dirección", default=None)
    Rooms = models.IntegerField(verbose_name="Habitaciones", default=None)
    Descriptions = models.CharField(max_length=50, verbose_name="Descripcion Empresa", default=None)
    UserId = models.ForeignKey('registration.UserProfile', on_delete=models.CASCADE, default=None)
 # Staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class RoomsType(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    RoomsDescription = models.CharField(max_length=50, default = None)

    def __str__(self):
        return self.RoomsDescription

class Features(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)  
    Element = models.CharField(max_length=50, default=None)
    Quantity = models.IntegerField(default=None)
    #RoomsId = models.ManyToManyField('Rooms')
    
    def __str__(self):
        return self.Element + ' Cantidad : '+ str(self.Quantity) +' / ' + str(self.Id)

    
class Rooms(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    HotelId = models.ForeignKey('Hotels', on_delete=models.CASCADE, default=None)
    RoomsName = models.CharField(max_length=50, default=None)
    RoomsCapacity = models.IntegerField(default=None)
    RoomsPrice = models.IntegerField(default=None)
    RoomsIs_active = models.BooleanField(default=None)
    RoomsTypeId = models.ForeignKey('RoomsType', on_delete=models.CASCADE, default = None)
    FeaturesId = models.ManyToManyField(Features)
    # FeaturesId = models.ForeignKey('Features', on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.RoomsName

# class Category(models.Model):
#     Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
#     CategoryDescription = models.CharField(max_length=50, verbose_name="Categoria",default = None)

#     def __str__(self):
#         return self.CategoryDescription

class PaymentMethod(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    PaymentMethodDescription = models.CharField(max_length=50, verbose_name="Metodo de pago",default = None)
    
    def __str__(self):
        return self.PaymentMethodDescription

class Client(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID", default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, verbose_name="Nombre", default = None)
    LastName = models.CharField(max_length=50, verbose_name="Apellidos", default = None)
    Rut = models.CharField(max_length=50, verbose_name="Rut", default = None)
    Address = models.CharField(max_length=50, verbose_name="Dirección", default = None)
    Phone = models.CharField(max_length=50, verbose_name="Telefono", default = None)
    Email = models.CharField(max_length=50, verbose_name="Correo Electronico", default = None)
    Nationality = models.CharField(max_length=50, verbose_name="Nacionalidad", default = None)
    #BookingId = models.ForeignKey('Booking', on_delete=models.CASCADE, default=None) 

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {} / {}'.format(self.Name, self.LastName, self.Rut)

class Payment(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    IdHotel = models.ForeignKey('Hotels', on_delete=models.CASCADE, default=None)
    Mount = models.IntegerField(verbose_name="Monto", default = None)
    IdBook = models.ForeignKey('Booking', on_delete=models.CASCADE, default=None)
    Date = models.DateTimeField(verbose_name="Fecha de pago",auto_now_add=True)
    PaymentMethodId = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'Hotel : '+ self.IdHotel.Name + ' / Cliente : '+ self.IdBook.BookingClientId.Name+' '+ self.IdBook.BookingClientId.LastName + ' ChechIn + : ' + str(self.IdBook.DateCheckIn) +' CheckOut - : '+ str(self.IdBook.DateCheckOut) + ' Fecha : ' + str(self.Date)

    class Meta:
        db_table = 'Payment'
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


class Booking(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    Created = models.DateTimeField(auto_now=True)
    RoomsId = models.ForeignKey(Rooms, verbose_name="Cabaña reservada", on_delete=models.CASCADE,default=None)
    #CreateBy = models.ForeignKey(UserProfile)
    DateCheckIn = models.DateField(verbose_name="Check In", default=datetime.now())
    # TimeCheckIn = models.TimeField(verbose_name="Hora CheckIn",default=None)
    DateCheckOut = models.DateField(verbose_name="CheckOut",default=datetime.now() + timedelta(days=2))
    # TimeCheckOut = models.TimeField(verbose_name="Hora CheckOut",default=None)
    #test = models.CharField(max_length = 50, default=None)
    Prepaid = models.BooleanField(verbose_name="Prepagado",default=None)
    no_of_guests=models.IntegerField(default=1)
    AubscriberMount = models.IntegerField(verbose_name="Monto Pendiente", default=None)
    #PaymentId = models.ForeignKey('Payment', on_delete=models.CASCADE, default=None)
    Is_Active = models.BooleanField(default=True)
    BookingClientId = models.ForeignKey(Client, on_delete=models.CASCADE) 
    HotelsId = models.ForeignKey(Hotels, on_delete=models.CASCADE, default=None, verbose_name="Hotel")
    check_out=models.BooleanField(default=False)

    def __str__(self):
        return (self.BookingClientId.Name+' '+ self.BookingClientId.LastName + ' ChechIn + : ' + str(self.DateCheckIn) +' CheckOut - : '+ str(self.DateCheckOut))

    # def charge(self):
    #     if self.check_out:
    #         if self.DateCheckIn==self.DateCheckOut:
    #             return self.room.rate
    #         else:
    #             time_delta = self.DateCheckOut - self.DateCheckIn
    #             total_time = time_delta.days
    #             total_cost = total_time*self.RoomsId.RoomsPrice
    #             # return total_cost
    #             return total_cost
    #     else:
    #         return 'calculated when checked out'   

# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['title']

#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ['headline']

#     def __str__(self):
#         return self.headline

# @receiver(post_save,sender=Booking)
# def RType(sender, instance, created, **kwargs):
#     room = instance.RoomsId
#     if created:
#         room.RoomsIs_active = False
#     room.save()
#     if instance.check_out ==True:
#         room.RoomsIs_active=True
#     room.save()   