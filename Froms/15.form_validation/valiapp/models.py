from django.db import models

class Info(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=8)
    country=models.CharField(max_length=10)
