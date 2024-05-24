from django.db import models
from account.models import KhachHang
from products.models import SanPham

# Create your models here.
class Cart(models.Model):
    UserName = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name='KhachHang_Cart')
    ProductId = models.ForeignKey(SanPham, on_delete=models.CASCADE, related_name='SanPham_Cart')
    SoLuong = models.IntegerField(default=1)
    ThanhTien = models.IntegerField(default=0)