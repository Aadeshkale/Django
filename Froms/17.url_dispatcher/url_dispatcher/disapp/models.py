from django.db import models

class Info(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=10)
    date=models.DateField(auto_now_add=True)
    
