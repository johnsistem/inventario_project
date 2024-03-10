from django.db import models

# Create your models here.
class Product(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   brand = models.CharField(max_length=50)
   price = models.DecimalField( max_digits=5, decimal_places=2 )
   stock_min = models.IntegerField()
   stock_max = models.IntegerField()

