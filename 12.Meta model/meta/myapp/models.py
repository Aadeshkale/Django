from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    sal=models.IntegerField()
    def __str__(self):
        return self.name 
    class Meta:
        db_table='Employee'         # change database name   
        ordering=['name']           # ording in asseending order on name coloumn for reverse use ['-name']
        unquie_together=['name','pune']