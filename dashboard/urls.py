from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('LoaiSP', views.list_LoaiSP, name='LoaiSP'),
    path('Them_LoaiSP', views.Them_LoaiSP, name='Them_LoaiSP'),
    path('Xoa_LoaiSP/<int:loai_id>/', views.Xoa_LoaiSP, name='Xoa_LoaiSP'),
    path('Sua_LoaiSP/<int:loai_id>/', views.Sua_LoaiSP, name='Sua_LoaiSP'),

    path('NhaCungCap', views.list_NhaCungCap, name='NhaCungCap'),
    path('Them_NCC', views.Them_NCC, name='Them_NCC'),
    path('Xoa_NCC/<int:ncc_id>/', views.Xoa_NCC, name='Xoa_NCC'),
    path('Sua_NCC/<int:ncc_id>/', views.Sua_NCC, name='Sua_NCC'),

    path('SanPham', views.list_SanPham, name='SanPham'),
    path('Them_SanPham', views.Them_SanPham, name='Them_SanPham'),
    path('Xoa_SP/<int:sp_id>/', views.Xoa_SP, name='Xoa_SP'),
    path('Sua_SP/<int:sp_id>/', views.Sua_SP, name='Sua_SP'),
    path('XemCT_SP/<int:sp_id>/', views.XemCT_SP, name='Xem_SP'),
    
    path('HoaDon', views.list_HoaDon, name='HoaDon'),
    path('XemCT_HD/<int:MaHD>/', views.receiptdetails, name='Xem_HoaDon'),
    path('Huy/<int:MaHD>/', views.cancelOrder, name='Huy_HoaDon'),
    path('XacNhan/<int:MaHD>/', views.ConfirmOrder, name='XacNhan_HoaDon'),


    path('Phieu_Nhap', views.list_PhieuNhap, name='Phieu_Nhap'),
    path('LapPhieuNhap', views.LapPhieuNhap, name='LapPhieuNhap'),
    path('XemCTPN/<int:MaPhieuNhap>/', views.XemCTPN, name='Xem_PhieuNhap'),
    path('Xoa_PN/<int:id>/', views.Xoa_PN, name='Xoa_PN'),
    
    
    path('NhanVien', views.list_NhanVien, name='NhanVien'),
    path('KhachHang', views.list_KhachHang, name='KhachHang'),
]