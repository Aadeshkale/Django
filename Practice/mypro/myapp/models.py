from django.db import models

class Reg(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    gender=models.CharField(max_length=20)
    country=models.CharField(max_length=10)