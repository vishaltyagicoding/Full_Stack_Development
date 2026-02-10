from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        # Save the user profile to the database
        from .models import UserProfile
        UserProfile.objects.create(name=name, email_id=email_id, password=password)
        return render(request, 'signal_email/success.html')
    else:
        return render(request, 'signal_email/register.html')
