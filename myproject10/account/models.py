from django.db import models

# Create your models here.

class Profile(models.Model):
    Name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name
