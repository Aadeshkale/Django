from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    year=models.IntegerField()

class Author(models.Model):
    book=models.ForeignKey(Book,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=20)

