from django.db import models

class Product(models.Model):
    productId=models.AutoField(primary_key=True)
    productName=models.CharField(max_length=20)
    productCost=models.IntegerField()
    productQuantity=models.IntegerField()
    productDescription=models.CharField(max_length=50,blank=True)

    obj=models.Manager()
    class Meta:
        db_table='product'
        ordering=['productQuantity']
        indexes=[
            models.Index(fields=['productName'])
        ]

# proapp_product