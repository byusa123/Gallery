from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    country =models.CharField(max_length=255)
    accounttype =models.CharField(max_length=255)    


class Gallery(models.Model):
    image = models.ImageField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField()
  
    
    def _str_(self):
        return self.location   