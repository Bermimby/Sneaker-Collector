from django.db import models
from django.urls import reverse

# Create your models here.
class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
     return self.brand
    

    def get_absolute_url(self):
       return reverse('detail', kwargs={'sneaker_id': self.id})
    

   
