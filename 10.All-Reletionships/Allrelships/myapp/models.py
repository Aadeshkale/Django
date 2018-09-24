from django.db import models

# Create your models here.
class Publisher(models.Model):
    pname=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return self.pname

class Author(models.Model):
    aname=models.CharField(max_length=20)
    aemail=models.EmailField(max_length=100)
    def __str__(self):
        return self.aname
    

class Student(models.Model):
    sname=models.CharField(max_length=20)
    sfee=models.IntegerField()
    def __str__(self):
        return self.sname
    

class Book(models.Model):
    publisher=models.OneToOneField(Publisher,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    student=models.ManyToManyField(Student)
    bname=models.CharField(max_length=20)
    bprice=models.IntegerField()
    def __str__(self):
        return self.bname
    