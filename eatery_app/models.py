from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=25)
    # menu = models.urlField()

    def __str__(self):
        return self.name


