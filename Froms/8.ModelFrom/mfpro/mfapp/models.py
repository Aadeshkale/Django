from django.db import models

class Stu(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=100)
    location=models.CharField(max_length=20)
        