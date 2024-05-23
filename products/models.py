import datetime
import os
from django.db import models
# Create your models here.
class NhaCungCap(models.Model):
    TenNCC = models.CharField(max_length=200)
    DiaChi = models.CharField(max_length=200)
    Email =models.CharField(max_length=200)
    SDT = models.CharField(max_length=20)
    WebSite = models.CharField(max_length=200)
    
    def __str__(self):
        return self.TenNCC

class LoaiSP(models.Model):
    TenLoai = models.CharField(max_length= 100)
    def __str__(self):
        return self.TenLoai

# def filepath(request, filename):
#     old_filename = filename
#     timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
#     filename = "%s%s" %(timenow, old_filename)
#     return os.path.join('img/', timenow)

class SanPham(models.Model):
    TenSP = models.CharField(max_length=255)
    Soluong = models.IntegerField()
    GiaNhap = models.IntegerField()
    GiaBan = models.IntegerField()
    MaLoai = models.ForeignKey(LoaiSP, on_delete=models.CASCADE)
    MaNCC = models.ForeignKey(NhaCungCap, on_delete=models.CASCADE)
    Mota = models.TextField()
    TrangThai = models.BooleanField(default=True)
    Anh = models.ImageField(upload_to='img', blank=True, null=True, default= None)
    TenThietBi = models.CharField(max_length=255)


# class HinhAnh(models.Model):
#     img = models.ImageField(null = True, blank= True, upload_to= filepath )


# //rút ngắn mô tả
# def chuyen_ngan_chuoi(chuoi, gioi_han_tu):
#     cac_tu = chuoi.split()
#     if len(cac_tu) <= gioi_han_tu:
#         return chuoi
#     else:
#         return ' '.join(cac_tu[:gioi_han_tu]) + '...'


# def format_gia_tien(gia):
#     gia_str = str(gia)
#     if len(gia_str) <= 3:
#         return gia_str
    
#     parts = []
#     while gia_str:
#         parts.append(gia_str[-3:])
#         gia_str = gia_str[:-3]
#     return '.'.join(reversed(parts))

