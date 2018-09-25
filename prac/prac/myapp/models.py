from django.db import models

# Create your models here.

class Common(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    class Meta:
        abstract=True    
    def __str__(self):
        return self.name

class Emp(Common):
    sal=models.IntegerField()    
    def __str__(self):
        return self.name

class Student(Common):
    fee=models.IntegerField() 
    def __str__(self):
        return self.name
       