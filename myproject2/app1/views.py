from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    student_list = [
        {'name': 'Alice', 'age': 22},
        {'name': 'Bob', 'age': 24},
        {'name': 'Charlie', 'age': 23},
        {'name': 'David', 'age': 25}
    ]
    return render(request, 'app1/about.html', {"students": student_list})

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        return HttpResponse(f'Form submitted! Name: {name}')
    return HttpResponse('Invalid request method')
