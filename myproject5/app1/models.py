from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrolled_date = models.DateField()
    city = models.CharField(max_length=100, default="")

    # def __str__(self):
    #     return self.name