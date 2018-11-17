from django.db import models

class Common(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        abstract=True

class Student(Common,models.Model):
    subject=models.CharField(max_length=20)

class Coustmer(Common,models.Model):
     payment=models.IntegerField()

