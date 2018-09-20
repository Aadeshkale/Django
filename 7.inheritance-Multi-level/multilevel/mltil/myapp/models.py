from django.db import models

# Create your models here.

# multi-level inheritance 

class Coustmer(models.Model):
    cname=models.CharField(max_length=20)
    csals=models.IntegerField()


class Employee(Coustmer):                                    # inheriting propertie from Coustermer classs 
    ename=models.CharField(max_length=20)                    # cname , csals  
    esal=models.IntegerField()
    
class Student(Coustmer):                                     # inheriting properties of Coutermer,Employee class
    sname=models.CharField(max_length=20)                    # cname, csals , ename , esal                           
    sfee=models.IntegerField()