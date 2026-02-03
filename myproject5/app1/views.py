from django.shortcuts import render
from .models import Students

def home(request):
    students = Students.objects.all()
    
    # Get unique cities for filter dropdown
    cities = Students.objects.values_list('city', flat=True).distinct().order_by('city')
    
    # If you want to get field names dynamically
    field_names = ['ID', 'Name', 'Age', 'Email', 'Enrollment Date', 'City']
    # Or use model fields:
    # field_names = [field.name for field in Students._meta.get_fields() if field.concrete]
    
    return render(request, 'home.html', {
        'students': students,
        'field_names': field_names,
        'cities': cities,
    })