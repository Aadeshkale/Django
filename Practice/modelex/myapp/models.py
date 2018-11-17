from django.db import models

class Stu(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
