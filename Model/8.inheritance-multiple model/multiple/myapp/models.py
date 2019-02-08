from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.AutoField(primary_key=True)                   # solveing problem of default id field 
    name=models.CharField(max_length=20)
class Coustmer(models.Model):
    cid=models.AutoField(primary_key=True)                   # solveing problem of default id field               
    loc=models.CharField(max_length=20)    

class Student(Employee,Coustmer):
    fee=models.IntegerField()    