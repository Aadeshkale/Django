from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    