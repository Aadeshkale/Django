from django.db import models

class Reg(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField(max_length=10)
    address=models.CharField(max_length=20)
    # other form fields 
    gender=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    city=models.CharField(max_length=50)    
    
    obj=models.Manager()
    class Meta:
        db_table='reg'
