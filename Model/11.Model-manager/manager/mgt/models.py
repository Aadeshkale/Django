from django.db import models

# Create your models here.
class Emp(models.Model):
    

    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,default='sample@gamil.com')
    obj=models.Manager()                                                # renameing default objects to obj 
    def __str__(self):
        return self.name
    