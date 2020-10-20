from django.shortcuts import render

# Create your views here.
def registration(request):
    context ={}
    return render(request,'registration.html', context)