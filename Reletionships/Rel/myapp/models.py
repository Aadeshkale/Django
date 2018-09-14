from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    cname=models.CharField(max_length=20)
    cfee=models.IntegerField()
