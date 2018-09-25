from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Coust(Emp):
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Std(Coust):
    fees=models.IntegerField()
    def __str__(self):
        return self.name
    
