from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.ImageField()
    loc=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    student=models.ManyToManyField(Student)
    cname=models.CharField(max_length=20)
    cfee=models.ImageField()
    def __str__(self):
        return self.cname
    