from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    mobile=models.IntegerField()
    address=models.CharField(max_length=60)
    def __str__(self):
        return self.name
class Depart(Emp):
    emp=models.OneToOneField(Emp)
    dname=models.CharField(max_length=10)
    dfee=models.IntegerField()
    def __str__(self):
      return self.dname

