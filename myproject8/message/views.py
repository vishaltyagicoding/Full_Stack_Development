from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_message(request):
    messages.success(request, 'Your form is submitted successfully!')
    messages.error(request, 'There was an error with your submission.')
    messages.info(request, 'Here is some information for you.')
    messages.debug(request, 'Debug information for developers.')
    messages.warning(request, 'This is a warning message.')
    return render(request, 'message.html')
