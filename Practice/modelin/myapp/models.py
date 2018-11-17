from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    
class Employee(models.Model):
    cid=models.AutoField(primary_key=True)
    address=models.CharField(max_length=20)

class Custmor(Student,Employee):
    loc=models.CharField(max_length=20)
