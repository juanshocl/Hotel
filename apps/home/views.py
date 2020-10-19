from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

# class index(ListView):
#     template_name = 'home/templates/index.html'

def index(request):
    context ={}
    return render(request,'index.html', context)