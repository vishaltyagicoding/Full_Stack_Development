from django.shortcuts import render
from django.core.mail import send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
# def send_bulk_email(request):
#     # Define the email data
#     email_data = [
#         ('Subject 1', 'Message body for email 1', 'alberttyagi123@gmail.com', ['pythonbyvishal@gmail.com']),
#         ('Subject 2', 'Message body for email 2', 'alberttyagi123@gmail.com', ['recipient2@example.com']),
#         ('Subject 3', 'Message body for email 3', 'alberttyagi123@gmail.com', ['recipient3@example.com']),
#     ]
#     # Send the emails
#     send_mass_mail(email_data, fail_silently=False)
#     return HttpResponse("Bulk emails sent successfully!")


def send_bulk_email(request):
    subject = "Bulk Email Subject"
    from_email = "alberttyagi123@gmail.com"
    recipient_list = ['pythonbyvishal@gmail.com', 'abc@gmail.com']

    html = render_to_string('bulkmail/email_template.html', {'name': 'Vishal'})
    
    email = EmailMultiAlternatives(subject, body=html, from_email=from_email, to=recipient_list)
    email.attach_alternative(html, "text/html")
    # email.attach_file('path/to/attachment.pdf')  # Optional: Attach a file
    email.send(fail_silently=False)
    return HttpResponse("Bulk emails sent successfully!")