from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
# def send_email(request):
#     if request.method == 'POST':
#         subject = request.POST['subject']
#         message = request.POST['message'] 
#         recipient = request.POST['recipient']
        
#         send_mail(subject, message, 'alberttyagi123@gmail.com', [recipient])
#         return HttpResponse('Email sent successfully!')

#     else:
#         return render(request, 'email_app/email_form.html')
    
# second way to send email is using EmailMessage class
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = render_to_string('email_app/email_template.html', {'message': request.POST['message']})
        recipient = request.POST['recipient']
        
        email = EmailMessage(subject, message, 'alberttyagi123@gmail.com', [recipient])
        email.content_subtype = 'html'
        email.send()
        return HttpResponse('Email sent successfully!')

    else:
        return render(request, 'email_app/email_form.html')