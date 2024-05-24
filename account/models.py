from django.db import models
from products.models import SanPham
# Create your models here.
class Account(models.Model):
    UserName = models.CharField(max_length=100, primary_key=True)
    Password = models.CharField(max_length=100)
    Quyen = models.CharField(max_length=100)
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)

class NhanVien(models.Model):
    MaNV = models.CharField(max_length=100, primary_key=True)
    TenNV = models.CharField(max_length=100)
    GioiTinh = models.CharField(max_length=100)
    NgaySinh = models.DateField()
    Email = models.CharField(max_length=100, unique=True)
    SoDT = models.CharField(max_length=100)
    DiaChi = models.CharField(max_length=100)
    UserName = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Account_NhanVien')

class KhachHang(models.Model):
    MaKH = models.AutoField(primary_key=True)
    TenKH = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    SoDT = models.CharField(max_length=100)
    DiaChi = models.CharField(max_length=100)
    UserName = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Account_KhachHang')

class YeuThich(models.Model):
    UserName = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name='KhachHang_YeuThich')
    ProductId = models.ForeignKey(SanPham, on_delete=models.CASCADE, related_name='SanPham_YeuThich')

class HoaDon(models.Model):
    MaHD = models.AutoField(primary_key=True)
    NgayLap = models.DateField()
    TongTien = models.IntegerField()
    PhuongThucVanChuyen = models.CharField(max_length=100, default='Giao Nhanh')
    PhiVanChuyen = models.IntegerField(default=0)
    TrangThai = models.CharField(max_length=100, null=True)
    PhuongThucThanhToan = models.CharField(max_length=100, default='COD')
    GhiChu = models.TextField(null=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name='KhachHang_HoaDon')

class ChiTietHD(models.Model):
    MaCTHD = models.AutoField(primary_key=True)
    MaHD = models.ForeignKey(HoaDon, on_delete=models.CASCADE, related_name='HoaDon_ChiTietHD')
    MaSP = models.ForeignKey(SanPham, on_delete=models.CASCADE, related_name='SanPham_ChiTietHD')
    SoLuong = models.IntegerField()
    ThanhTien = models.IntegerField()