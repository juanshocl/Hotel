from django.core.checks.messages import Error
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.booking.models import *
from apps.booking.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


# Create your views here.
# def bookingHome(request):
#     context ={}
#     return render(request,'booking.html', context)

class bookingHome(ListView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking1.html'
    success_url = reverse_lazy('bookingHome')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {}
        try:
            action = request.POST['action']
            if action == 'create_client':
                print(request.POST)
                pass
                # with transaction.atomic():
                #     frmClient = ClientForm(request.POST)
                #     data = frmClient.save()
            elif action == 'create_booking':
                print(request.POST)
                pass
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de reservas'
        return context

class Calendar(ListView):
    model = Booking
    form_class = BookingForm
    template_name = 'Calendar/calendar3.html'
    success_url = reverse_lazy('calendar')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de reservas'
        return context
        
class ClientsListView(ListView):
    model = Client
    template_name = 'Client/cliente.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title' ] = 'Listado de Clientes'
        context['lazy_url'] = reverse_lazy('bookingHome')
        return context
    

def ClientList(request):
    data = {
        'title' : 'Listado de Clientes',
        'clientes' : Client.objects.all()

    }
    return render(request,'Client/cliente.html', data)

# class ClientsCreateView(CreateView):
#     model = Client
#     form_class = ClientForm
#     template_name = 'Client/create.html'
#     success_url = reverse_lazy('booking:ClientList')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title' ] = 'Creacion de Clientes'
#         return context

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

class ClientsCreateView(CreateView):
    model = Client
    form_classes = ClientForm

    template_name = 'Client/create.html'
    success_url = reverse_lazy('bookingHome')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(ClientsCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Creación de Clientes'
        context['lazy_url'] = reverse_lazy('bookingHome')
        # context['action'] = 'addCli'

        return context

    # def ClientForm_form_valid(self, form):
    #     return form.ClientForm(self.request, redirect_url=self.get_success_url())

    # def BookingForm_form_valid(self, form):
    #     # user = form.BookingForm(self.request)
    #     return form.BookingForm(self.request, redirect_url=self.get_success_url())



class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'Client/addclient.html'
    success_url = reverse_lazy('bookingHome')
    cliente = ''
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    form = self.form_class(request.POST)
               #     BookingForm(request.POST)
                    if form.is_valid:
                        print(request.POST)
                        form.save()
                    else:
                        data['error']  = form.errors
            elif action == 'addCli':
                with transaction.atomic():
                    # cliente = '{} {} / {}'.format(request.POST['Name'], request.POST['LastName'], request.POST['Rut'])
                    frmClient = ClientForm(request.POST)
                    if frmClient.is_valid:
                        frmClient.save()
                    else:
                        data['error']  = frmClient.errors
            else:
                data['error'] =  "No se ha ingresado a ninguna opcion"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de reservas'
        context['ruta'] = 'Creacion Reservas'
        context['urlbooking'] = reverse_lazy('bookingHome')
        context['frmClient'] = ClientForm()
        context['action'] = 'add'
        # context['cliente'] = self.cliente
        return context


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'Add.html'
    success_url = reverse_lazy('ClientList')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de metodo de pago'
        return context

# Quedamos hasta acá #######
class PaymentmethodCreateView(CreateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = 'Add.html'
    success_url = reverse_lazy('ClientList')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de metodo de pago'
        return context
        
# class RoomsCreateView(CreateView):
#     model = Rooms
#     form_class = RoomsForm
#     template_name = 'Add.html'
#     success_url = reverse_lazy('ClientList')
    

#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     # def post(self, request, *args, **kwargs):
#     #     data = {}
#     #     try:
#     #         action = request.POST['action']
#     #         if action == 'add':
#     #             form = self.get_form()
#     #             data = form.save()
#     #         else:
#     #             data['error'] = 'No ha ingresado a ninguna opción'
#     #     except Exception as e:
#     #         data['error'] = str(e)
#     #     return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creación de Habitaciones'
#         return context

class RoomsCreateView(CreateView):
    model = Rooms
    form_class = RoomsForm
    template_name = 'Add.html'
    success_url = reverse_lazy('ClientList')
    

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Caracteristicas'
        return context

class FeatureCreateView(CreateView):
    model = Features
    form_class = FeatureForm
    template_name = 'Add.html'
    success_url = reverse_lazy('ClientList')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Caracteristicas'
        return context

class RoomstypeCreateView(CreateView):
    model = RoomsType
    form_class = RoomsTypeForm
    template_name = 'Add.html'
    success_url = reverse_lazy('ClientList')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Tipos de habitacion'
        return context

class HotelCreateView(CreateView):
    model = Hotels
    form_class = HotelForm
    template_name = 'Add.html'
    success_url = reverse_lazy('ClientList')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Hoteles'
        return context


