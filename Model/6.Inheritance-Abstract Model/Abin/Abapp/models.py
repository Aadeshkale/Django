from django.db import models

# Create your models here.

# creating Abstract model inheritance 

class Common(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    class Meta:                              # creating class abstract by using meta information                                   
        abstract = True        

class Student(Common):                       # inheriting name , loc from common abs class                          
    fee=models.IntegerField()

class Coustmer(Common):                      # inheriting name , loc from common abs class   
    sales=models.IntegerField()

class Employee(Common):
    salary=models.IntegerField()             # inheriting name , loc from common abs class   