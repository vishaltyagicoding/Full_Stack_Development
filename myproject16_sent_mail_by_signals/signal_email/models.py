from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
