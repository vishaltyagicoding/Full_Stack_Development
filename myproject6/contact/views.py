from django.shortcuts import render, redirect
from contact.models import ContactMessage
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Process the form data (e.g., save to database, send email, etc.)
        if name and message and email:
            contact_message = ContactMessage.objects.create(name=name, email=email, message=message)
            contact_message.save()
            return HttpResponse(f"Thank you, {name}, for your message!")
        
        else:
            return HttpResponse("Please provide both name and message.")
    
    return redirect('home')