from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Course(models.Model):
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)   # mapping one to one relationship with mode
    cname=models.CharField(max_length=20)
    cfee=models.IntegerField()
    def __str__(self):
        return self.cname
