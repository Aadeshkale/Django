from django.db import models

# Create your models here.
class Publisher(models.Model):
    pname=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)

class Author(models.Model):
    aname=models.CharField(max_length=20)
    aemail=models.EmailField(max_length=100)

class Student(models.Model):
    sname=models.CharField(max_length=20)
    sfee=models.IntegerField()

class Book(models.Model):
    publisher=models.OneToOneField(Publisher,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    student=models.ManyToManyField(Student)
    bname=models.CharField(max_length=20)
    bprice=models.IntegerField()