from django.db import models

class Reg(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    gender=models.CharField(max_length=20)
    country=models.CharField(max_length=10)
    obj=models.Manager()
    class Meta:
        db_table='reg' 
        