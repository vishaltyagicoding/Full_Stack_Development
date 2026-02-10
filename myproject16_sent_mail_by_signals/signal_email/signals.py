from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.core.mail import send_mail

@receiver(post_save, sender=UserProfile)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Our Site!"
        message = f"Hello {instance.name}, welcome to our site! We're glad to have you here."
        send_mail(
            subject,
            message,
            'alberttyagi123@gmail.com',
            [instance.email_id],
            fail_silently=False,
        )
