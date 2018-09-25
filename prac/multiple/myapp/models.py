from django.db import models

# Create your models here.
class Emp(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Cst(models.Model):
    cid=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=20)
    def __str__(self):
        return self.email
       
class Std(Emp,Cst):
    fee=models.IntegerField()
    def __str__(self):
        return self.name
    