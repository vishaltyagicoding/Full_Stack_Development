from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyModel
# Create your views here.

def home(request):
    return HttpResponse("Hello, welcome to my Django project!")


def about(request):
    data = MyModel.objects.all()
    return render(request, 'about.html', {'data': data})



