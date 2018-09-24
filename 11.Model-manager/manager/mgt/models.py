from django.db import models

class Emp(models.Model):
         
      name=models.CharField(max_length=20)
      email=models.EmailField( max_length=20)
      loc=models.CharField(max_length=20)
         
      obj=models.Manager()               # rename default manager 'objects' to 'obj'  
      def __str__(self):
          return self.name
            