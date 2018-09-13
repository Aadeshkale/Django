from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=10)
    def __str__(self):
         return self.name 

class Course(models.Model):
    student=models.ForeignKey(Student)               # many to one reletionship i.e ForeignKey
    cname=models.CharField(max_length=20)
    def __str__(self):
        return self.cname
