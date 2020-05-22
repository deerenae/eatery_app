from django.db import models
# from django.contrib.auth.models import User 

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    menu = models.URLField(max_length=200, default='https://www.google.com/')

    def __str__(self):
        return self.name


