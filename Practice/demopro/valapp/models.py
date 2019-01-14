from django.db import models

class Info(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    
