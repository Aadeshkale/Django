from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name