from django.shortcuts import render
from .forms import ProfileForms
from .models import Profile
from django.contrib import messages

# Create your views here.
def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile uploaded successfully!')
        else:
            messages.error(request, 'Failed to upload profile. Please correct the errors below.')
    else:
        form = ProfileForms()
    return render(request, 'upload_profile.html', {'form': form})

def view_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'view_profiles.html', {'profiles': profiles})

