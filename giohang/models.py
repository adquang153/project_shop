from django.db import models
from sanpham.models import Variation
from khachhang.models import CustomerUser
from django.utils import timezone
# Create your models here.

class Cart(models.Model):
#     created_at = models.DateTimeField(default = timezone.now)
#     updated_at = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(CustomerUser, on_delete= models.CASCADE)
    title = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return models.created_at
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return models.cart
    