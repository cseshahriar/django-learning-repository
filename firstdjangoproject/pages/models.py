from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=125, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=15)

    objects = models.Manager 
