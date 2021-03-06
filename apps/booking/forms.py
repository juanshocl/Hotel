from datetime import datetime

from django import forms
from django.forms import ModelForm, Form, ModelChoiceField
from django.forms.widgets import Select

from apps.booking.models import *
from apps.registration.models import UserProfile



# class CategoryForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # for form in self.visible_fields():
#         #     form.field.widget.attrs['class'] = 'form-control'
#         #     form.field.widget.attrs['autocomplete'] = 'off'
#         self.fields['name'].widget.attrs['autofocus'] = True

#     class Meta:
#         model = Category
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese un nombre',
#                 }
#             ),
#             'desc': forms.Textarea(
#                 attrs={
#                     'placeholder': 'Ingrese un nombre',
#                     'rows': 3,
#                     'cols': 3
#                 }
#             ),
#         }

#     def save(self, commit=True):
#         data = {}
#         form = super()
#         try:
#             if form.is_valid():
#                 form.save()
#             else:
#                 data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return data


# class ProductForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs['autofocus'] = True

#     class Meta:
#         model = Product
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese un nombre',
#                 }
#             ),
#             'cat': forms.Select(
#                 attrs={
#                     'class': 'select2',
#                     'style': 'width: 100%'
#                 }
#             ),
#         }

#     def save(self, commit=True):
#         data = {}
#         form = super()
#         try:
#             if form.is_valid():
#                 form.save()
#             else:
#                 data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return data


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'class': 'col-sm',
                    'style': 'width: 50%',
                }
                
            ),
            'LastName': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos',
                    'class': 'col-sm',
                    'style': 'width: 50%',
                }
            ),
            'Rut': forms.TextInput(
                attrs={
                    'placeholder': 'Rut',
                    'class': 'col-sm',

                }
            ),
            'Address': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'Phone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefono',
                }
            ),
            'Email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'Nationality': forms.TextInput(
                attrs={
                    'placeholder': 'Nacionalidad',
                }
            )
        }

class HotelForm(ModelForm):
    class Meta:
        model = Hotels
        fields = '__all__'
        labels = {
            'UserId': ('Administrador'),
        }
        widgets = {
            'Name': forms.TextInput(
                attrs={
                     'placeholder': 'Nombre',
              }),
            'Rut': forms.TextInput(
                 attrs={
                     'placeholder': 'Rut',
                }
             ),
            'Address': forms.TextInput(
                 attrs={
                     'placeholder': 'Ingrese su dirección',
                 }
             ),
            'Rooms': forms.TextInput(
                 attrs={
                     'placeholder': 'Cantidad de habitaciones',
                 }
             ),
            'Descriptions': forms.TextInput( 
                attrs={
                     'placeholder': 'Descripción',
                 }),
            'UserId': 
            Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 50%'
                }),

        }

# class HotelForm(Form):
#     Name = forms.CharField(label ="Nombre", max_length=50,
#     widget=forms.TextInput(
#                 attrs={
#                      'placeholder': 'Nombre',
#               }))
#     Rut = forms.CharField(label ="Rut", max_length=50,
#     widget= forms.TextInput(
#                  attrs={
#                      'placeholder': 'Rut',
#                 }
#              ))
#     Address = forms.CharField(label ="Dirección", max_length=50,
#     widget=forms.TextInput(
#                  attrs={
#                      'placeholder': 'Ingrese su dirección',
#                  }
#              ))
#     Rooms = forms.IntegerField(required=False)
#     Descriptions = forms.CharField(label ="Descripción", max_length=50,
#     widget=forms.TextInput(
#                  attrs={
#                      'placeholder': 'Descripción',
#                  }
#              ))


#     UserId = forms.ModelChoiceField(queryset=UserProfile.objects.all()
#     , widget=Select(attrs={
#     'class': 'form-control select2',
#     'style': 'width: 100%'
#     })
#     )

    

# class HotelForm(ModelForm):
#     class Meta:
#         model = Hotels
#         fields = '__all__'
#         widgets = {
#             'Name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Nombre',
#                 }
#             ),
#             'Rut': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Rut',
#                 }
#             ),
#             'Address': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su dirección',
#                 }
#             ),
#             'Rooms': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Habitaciones',
#                 }
#             ),
#             'Descriptions': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Descripción',
#                 }
#             ),
#             'UserId': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Administrador',
#                 }
#             )
#         }

class RoomsTypeForm(ModelForm):
    class Meta:
        model = RoomsType
        fields = '__all__'
        labels = {
            'RoomsDescription': 'Que Tipo de Habitacion es?',

        }
        widgets = {
            'RoomsDescription': forms.TextInput(
                attrs={
                    'placeholder': 'Descrición Habitación',
                }
            )
        }

class FeatureForm(ModelForm):
    class Meta:
        model = Features
        fields = '__all__'
        labels = {
            'Element': ('Elemento'),
            'Quantity': ('Cantidad'),
            'RoomsId': ('Habitacion'),
        }
        widgets = {
            'Element': forms.TextInput(
                 attrs={
                     'placeholder': 'Elemento',
                 }),
            'Quantity': forms.TextInput(
                                 attrs={
                     'placeholder': 'Cantidad',
                 }
            ),
            # 'RoomsId': forms.Select(attrs={
            #     'class': 'form-control select2',
            #     'style': 'width: 100%'
            #     }),
        }






# class FeaturesForm(ModelForm):
#     class Meta:
#         model = Features
#         fields = '__all__'
#         widgets = {
#             'Element': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Elemento',
#                 }
#             ),
#             'Quantity': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Cantidad',
#                 }
#             ),

#         }
 
# class RoomsForm(Form):
#     RoomsCapacity = forms.IntegerField(
#         required=True
#     ,label ="Capacidad"
#     , 
#     widget= forms.TextInput(
#                  attrs={
#                      'placeholder': 'Capacidad',
#                  }
#              )
#     )
#     HotelId = forms.ModelChoiceField(queryset=Hotels.objects.all(), widget=forms.Select(attrs={
#     'class': 'form-control select2',
#     'style': 'width: 100%'
#     }))

#     RoomsPrice = forms.IntegerField(required=True
#     #,label ="Precio Habitacion"
#     # ,  
#     # widget= forms.TextInput(
#     #              attrs={
#     #                  'placeholder': 'Precio Habitacion',
#     #              }
#     #          )
#     )
#     RoomsIs_active = forms.BooleanField(required=True,label ="Habitacion activa?")
#     FeaturesId = forms.ModelMultipleChoiceField(queryset=Features.objects.all(), widget=forms.Select(attrs={
#     'class': 'form-control select2',
#     'style': 'width: 100%'
#     }))
#     RoomsTypeId = forms.ModelChoiceField(queryset=RoomsType.objects.all(), widget=forms.Select(attrs={
#     'class': 'form-control select2',
#     'style': 'width: 100%'
#     }))

class RoomsForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        labels = {
            'HotelId': ('Hotel'),
            'RoomsCapacity': ('Capacidad'),
            'RoomsName': ('Nombre Habitacion'),
            'RoomsPrice': ('Precio'),
            'RoomsIs_active': ('Esta operativa'),
            'RoomsTypeId': ('Tipo de habitacion'),
            'FeaturesId': ('Contiene'),
            
        }
        widgets = {
            'RoomsCapacity': forms.TextInput(
                attrs={
                    'placeholder': 'Capacidad de habitación',
                }
            ),
            'RoomsPrice': forms.TextInput(
                attrs={
                    'placeholder': 'Precio Habitacion',
                }
            ),
            'RoomsIs_active': forms.CheckboxInput(
            ),      
            'FeaturesId': forms.SelectMultiple(
                # queryset=Features.objects.all(),
                attrs={
                'class': 'form-control select2',
                'style': 'width: 50%',
                }
            )
        }

class PaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        widgets = {
            'PaymentMethodDescription': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            )
        }


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        labels = {
            'IdHotel': 'Hotel',
            'Mount' : 'Monto',
            'IdBook': 'Reserva',
            'PaymentMethodId' : 'Forma de pago',
        }
        widgets = {
            'Mount': forms.TextInput(
                attrs={
                    'placeholder': 'Monto',
                }
            ),
            # 'Date': forms.DateInput(
            #     attrs={
            #         'placeholder': 'Fecha',
            #     }
            # )
        }


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['RoomsId','DateCheckIn','DateCheckOut','Prepaid','AubscriberMount','HotelsId','BookingClientId','no_of_guests','check_out','Is_Active']
        labels = {
            'DateCheckIn': 'Fecha CheckIn',
            'HotelsId': 'Hotel',
            'BookingClientId': 'Cliente',
            'no_of_guests': 'Numero de visitantes',
            'check_out' : 'Check Out',
            'Is_Active': 'Disponible'

        }
        widgets = {
            'RoomsId': forms.Select(),
            'DateCheckIn': forms.SelectDateWidget(
                # format='%d-%m-%y %H:%M',
                # attrs={
                #     'value': datetime.now().strftime('%d-%m-%Y'),
                # }
            ),
            # 'TimeCheckIn': forms.TimeInput(
            #     attrs={
            #         'placeholder': 'Hora Checkin',
            #     }
            # ),
            'DateCheckOut': forms.SelectDateWidget(
                # format='%Y-%m-%d',
                # attrs={
                #     'value': datetime.now().strftime('%d-%m-%Y'),
                # }
            ),
            'no_of_guests': forms.TextInput(),
            # 'TimeCheckOut': forms.TimeInput(
            #     attrs={
            #         'placeholder': 'Hora CheckOut',
            #     }
            # ),
            'Prepaid': forms.CheckboxInput(
            ),
            'AubscriberMount': forms.TextInput(
                attrs={
                    'placeholder': 'Monto pendiente',
                }
            ),
            'Is_Active': forms.CheckboxInput(
            ),
            'BookingClientId': forms.Select(
                attrs={
                    'id': 'SelectBookingClientId'
                }
            ),
            'check_out': forms.CheckboxInput(
            ),
            'HotelsId': forms.Select(
                # attrs={
                #     'placeholder': 'Monto pendiente',
                # }
            )
        }
        # def save(self, commit=True):
        #     data = {}
        #     form = super()
        #     try:
        #         if form.is_valid:
        #             form.save()
        #         else:
        #             data['error']  = form.errors
        #     except Exception as e:
        #         data['error'] = str(e)
        #     return data





























    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             instance = form.save()
    #             data = instance.toJSON()
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data

# class publishForm(forms.Form):
    
#     name = forms.CharField(label ="Nombre", max_length=50)
#     #Type_advertisement = forms.
#     description = forms.CharField(label = "", max_length=200)
#     Userfacebook = forms.CharField(label = "", max_length=50)
#     UserInstagram = forms.CharField(label = "", max_length=50)
#     UserTwitter = forms.CharField(label = "", max_length=50)
#     #comuna = forms.
#     whatsapp = forms.CharField(label ="Whatsapp Formato (569XXXXXXXX)", max_length=11)
#     show_phones = forms.BooleanField(label ="¿Mostrar Telefono?", required=False)
#     email = forms.EmailField(label ="Email", required=False)
#     url_website = forms.URLField(label = "Sitio Web", required=False)
#     address = forms.CharField(max_length=200)
#     show_adress = forms.BooleanField(required=False)

#     # def clean(self):
#     #     cleaned = super().clean()
#     #     if len(cleaned['name']) <= 50:
#     #         raise forms.ValidationError('Validacion xxx')
#     #         # self.add_error('name', 'Le faltan caracteres')
#     #     return cleaned


# class TestForm(forms.Form):
#     categories = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
#         'class': 'form-control select2',
#         'style': 'width: 100%'
#     }))

#     products = forms.ModelChoiceField(queryset=Product.objects.none(), widget=forms.Select(attrs={
#         'class': 'form-control select2',
#         'style': 'width: 100%'z
#     }))

#     # search = CharField(widget=TextInput(attrs={
#     #     'class': 'form-control',
#     #     'placeholder': 'Ingrese una descripción'
#     # }))

#     search = forms.ModelChoiceField(queryset=Product.objects.none(), widget=forms.Select(attrs={
#         'class': 'form-control select2',
#         'style': 'width: 100%'
#     }))


# class SaleForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['cli'].queryset = Client.objects.none()

#     class Meta:
#         model = Sale
#         fields = '__all__'
#         widgets = {
#             'cli': forms.Select(attrs={
#                 'class': 'custom-select select2',
#                 # 'style': 'width: 100%'
#             }),
#             'date_joined': forms.DateInput(
#                 format='%Y-%m-%d',
#                 attrs={
#                     'value': datetime.now().strftime('%Y-%m-%d'),
#                     'autocomplete': 'off',
#                     'class': 'form-control datetimepicker-input',
#                     'id': 'date_joined',
#                     'data-target': '#date_joined',
#                     'data-toggle': 'datetimepicker'
#                 }
#             ),
#             'iva': forms.TextInput(attrs={
#                 'class': 'form-control',
#             }),
#             'subtotal': forms.TextInput(attrs={
#                 'readonly': True,
#                 'class': 'form-control',
#             }),
#             'total': forms.TextInput(attrs={
#                 'readonly': True,
#                 'class': 'form-control',
#             })
#         }
