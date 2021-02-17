from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.booking.models import *
from apps.booking.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.
def bookingHome(request):
    context ={}
    return render(request,'booking.html', context)


class ClientsListView(ListView):
    model = Client
    template_name = 'Client/cliente.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title' ] = 'Listado de Clientes'
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
    form_class = ClientForm
    template_name = 'Client/create.html'
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
        context['title'] = 'Creación de Clientes'
        return context




class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
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
        context['title'] = 'Creación de reservas'
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
        context['title'] = 'Creación de Tipos de habitacionS'
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


