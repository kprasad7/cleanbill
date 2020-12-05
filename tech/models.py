from django.db import models
from django.contrib.auth.models import User

class MyData(models.Model):
    phone=models.CharField(max_length=20)

    def __str__(self):  
        return self.phone 

class ShopData(models.Model):
    name=models.CharField(max_length=100)
    content=models.CharField(max_length=400)
    
    def __str__(self):  
        return  self.name + "----" + self.content