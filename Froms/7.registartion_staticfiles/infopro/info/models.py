from django.db import models

class Reg(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    obj=models.Manager()
    class Meta:
        db_table='reg'