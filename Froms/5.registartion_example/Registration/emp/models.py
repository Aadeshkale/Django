from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    sal=models.IntegerField()
    company=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    