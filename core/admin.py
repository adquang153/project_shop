from django.contrib import admin
from dathang.models import Order
from giohang.models import Cart,CartItem
from khachhang.models import CustomerUser
from sanpham.models import Product,Category
# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CustomerUser)
admin.site.register(Product)
admin.site.register(Category)

# admin.site.register()