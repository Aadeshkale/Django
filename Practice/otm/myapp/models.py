from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name
    

class Subject(models.Model):
    student=models.ManyToManyField(Student)
    name=models.CharField(max_length=20)   
    def __str__(self):
        return self.name
