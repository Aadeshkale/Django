from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=40)
    def __str__(self):
        return self.name+"->"+str(self.age)+"->"+self.address

class Course(models.Model):
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    cname=models.CharField(max_length=20)
    fname=models.CharField(max_length=10)
    def __str__(self):
        return self.cname+"->"+self.fname


