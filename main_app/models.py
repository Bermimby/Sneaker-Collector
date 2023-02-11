from django.db import models
from django.urls import reverse

# Create your models here.
BRANDS =(
   ('M', 'MGK'),
   ('K', 'Kizik'),
   ('C','Crep')
)
class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
     return self.brand
    

    def get_absolute_url(self):
       return reverse('detail', kwargs={'sneaker_id': self.id})

class Cleaner(models.Model):
    make=models.CharField(max_length=3)
    choices=BRANDS,
    default=BRANDS[0][0]
   
    sneaker= models.ForeignKey(Sneaker,on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.make}"

      





 
    

   
