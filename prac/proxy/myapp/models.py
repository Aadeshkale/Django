from django.db import models

# Create your models here.
class Std(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    obj=models.Manager()
    def __str__(self):
        return self.name

class Sproxy(Std):
    class Meta:
        proxy=True    

