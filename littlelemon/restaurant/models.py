from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def get_item(self):
        return f'{self.title} {str(self.price)}'

