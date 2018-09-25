from django.db import models

# Create your models here.

class Emp(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    sal=models.IntegerField()
    obj=models.Manager()
    def __str__(self):
        return self.name
    