from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.AutoField(primary=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=40)
    def __str__(self):
        return self.name


# creating proxy model for Student model

class Sproxy(Student):
    class Meta:
        proxy=True
