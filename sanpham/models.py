from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(default='',max_length=100)
    slug = models.CharField(default='',max_length=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(default='',max_length=255)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_img = models.CharField(max_length=255,default='')
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class Variation(models.Model):
    """Thay doi lien quan den san pham"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(default='',max_length=255) 
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    """Hang ton kho"""
    inventory = models.IntegerField(default=0) 
    active = models.BooleanField(default=True)