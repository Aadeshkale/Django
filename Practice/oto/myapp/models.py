from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    author=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        db_table="book"

class Publisher(models.Model):
    book=models.OneToOneField(Book,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=20)