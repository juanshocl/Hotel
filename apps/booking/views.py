from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.booking.models import Client


# Create your views here.
def booking(request):
    context ={}
    return render(request,'booking.html', context)

# class ClientList(ListView):
#     model = Client

class ClientsListView(ListView):
    model = Client
    template_name = 'Client/cliente.html'
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