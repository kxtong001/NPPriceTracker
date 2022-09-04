from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from asyncio.windows_events import NULL
from tkinter import CASCADE
import datetime
from datetime import timedelta

# Create your models here.
#Itemdetail by URL 
class Item(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    imageurl= models.URLField(default=NULL)
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price1 = models.FloatField(default=0)
    price2 = models.FloatField(default=0)
    price3 = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)




    def __str__(self):
        return str(self.name)
    
    



#prices of 1 item - not working as intended
class Itemprices(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(Item,default =0, on_delete=models.CASCADE)
    price = models.FloatField(blank=True)
    

    def __str__(self):
        return str(self.name)
