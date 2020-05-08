from django.db import models
from django.db.models.signals import post_save,pre_save,post_delete

class Author(models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

def post_singnal_handler(sender,instance,**kwargs):
    print("Data is inserted successfully")

def pre_singnal_handler(sender,instance,**kwargs):
    print("Action taken before data inserted")

post_save.connect(sender=Author,receiver=post_singnal_handler)

pre_save.connect(sender=Author,receiver=pre_singnal_handler)