from django.db import models

class File(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(max_length=255,upload_to='media')
    date=models.DateTimeField(auto_now_add=True)