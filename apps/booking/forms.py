from datetime import datetime

from django import forms
from django.forms import ModelForm

#from core.erp.models import Category, Product, Client, Sale
from apps.booking.models import Client


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
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            ),
            'LastName': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos',
                }
            ),
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
#         'style': 'width: 100%'
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
