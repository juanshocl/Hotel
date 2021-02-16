from django.db import models
from apps.registration.models import UserProfile

import uuid

class Hotels(models.Model):
    Id = models.UUIDField(primary_key=True, verbose_name="ID",default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50,verbose_name="Nombre Hotel", default=None)
    Rut = models.CharField(max_length=50, verbose_name="Rut Empresa", default=None)
    Address = models.CharField(max_length=50, verbose_name="Dirección", default=None)
    Rooms = models.IntegerField(verbose_name="Habitaciones", default=None)
    Descriptions = models.CharField(max_length=50, verbose_name="Descripcion Empresa", default=None)
    UserId = models.ForeignKey('registration.UserProfile', on_delete=models.CASCADE, default=None)

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
        return self.RoomsName +' / ' + str(self.Id)

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
        return (self.Name +' '+self.LastName)

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
    DateCheckIn = models.DateField(verbose_name="Fecha CheckIn",default=None)
    TimeCheckIn = models.TimeField(verbose_name="Hora CheckIn",default=None)
    DateCheckOut = models.DateField(verbose_name="Fecha CheckOut",default=None)
    TimeCheckOut = models.TimeField(verbose_name="Hora CheckOut",default=None)
    #test = models.CharField(max_length = 50, default=None)
    Prepaid = models.BooleanField(verbose_name="Prepagado",
    default=None)
    AubscriberMount = models.IntegerField(verbose_name="Monto PendienteS", default=None)
    #PaymentId = models.ForeignKey('Payment', on_delete=models.CASCADE, default=None)
    Is_Active = models.BooleanField
    BookingClientId = models.ForeignKey('Client', on_delete=models.CASCADE) 
    HotelsId = models.ForeignKey('Hotels', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return (self.BookingClientId.Name+' '+ self.BookingClientId.LastName + ' ChechIn + : ' + str(self.DateCheckIn) +' CheckOut - : '+ str(self.DateCheckOut))

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