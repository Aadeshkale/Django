from django.db import models
from django.db import models
# Create your models here.

class Student(models.Model):
    id=models.IntegerField()
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
