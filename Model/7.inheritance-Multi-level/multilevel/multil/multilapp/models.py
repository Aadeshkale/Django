from django.db import models

# Create your models here.

# multilevel inheritance model 

class Coustmer(models.Model):
    cname=models.CharField(max_length=20)
    csals=models.IntegerField()

class Employee(Coustmer):                                    # inherits properties from Coustmer class
    ename=models.CharField(max_length=20)                    # cname,csals   
    esal=models.IntegerField()

class Student(Employee):                                      # inherits propertis from Coustmer , Employee                   
    sname=models.CharField(max_length=20)                    # cname,csals ,ename,esal   
    sfee=models.IntegerField()

