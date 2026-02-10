from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_handler(sender, instance, **kwargs):
    # Example of a pre-save signal handler
    print(f"About to save Post with title: {instance.title}")

@receiver(post_save, sender=Post)
def post_save_handler(sender, instance, created, **kwargs):
    # Example of a post-save signal handler
    if created:
        print(f"New Post created with title: {instance.title}")
    else:
        print(f"Post updated with title: {instance.title}")