from django.db import models
from account.models import NhanVien
from products.models import SanPham, NhaCungCap

# Create your models here.

class PhieuNhap(models.Model):
    MaNV = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    NgayNhap = models.DateField()
    TrangThai = models.CharField(max_length=100)
    TongTien = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.TongTien = sum(
                chi_tiet.SoLuong * chi_tiet.GiaNhap
                for chi_tiet in self.chitietphieunhap_set.all()
            )
        super().save(*args, **kwargs)
    

class ChiTietPhieuNhap(models.Model):
    MaCTPN = models.AutoField(primary_key=True)
    MaPhieuNhap = models.ForeignKey(PhieuNhap, on_delete=models.CASCADE)
    MaSP = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    MaNCC = models.ForeignKey(NhaCungCap, on_delete=models.CASCADE)
    SoLuong = models.IntegerField()
    GiaNhap = models.IntegerField()

