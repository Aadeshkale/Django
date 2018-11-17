from django.db import models

# class Student(models.Model):
#     name=models.CharField(max_length=20)

# class Coustmer(Student):
#     payment=models.IntegerField()

# class Employee(Coustmer):
#     address=models.CharField(max_length=20)

class Coustmer(models.Model):
    cname=models.CharField(max_length=20)
    csals=models.IntegerField()

class Employee(Coustmer):                                    # inherits properties from Coustmer class
    ename=models.CharField(max_length=20)                    # cname,csals   
    esal=models.IntegerField()

class Student(Employee):                                      # inherits propertis from Coustmer , Employee                   
    sname=models.CharField(max_length=20)                    # cname,csals ,ename,esal   
    sfee=models.IntegerField()