from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductDb(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_code = models.IntegerField()
    category = models.TextField()
    price = models.IntegerField()
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name
    
