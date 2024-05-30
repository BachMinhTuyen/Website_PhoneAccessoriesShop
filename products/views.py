import os
from pyexpat.errors import messages
from django.contrib import messages
from urllib import request
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import Http404
from django.shortcuts import get_object_or_404
from products.forms import SanPhamForm
from phoneaccessorieswebsite_django import settings
from .models import LoaiSP, SanPham
from dashboard.models import NhaCungCap
from  django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

# ======================================================View cho khách hàng======================================
# Trang chính hiển thị sản phẩm
# def index(request):
#     return render(request, 'pages/SanPham.html')

# Thông tin toàn bộ sản phẩm cho KH
def DSSP(request):
    listLoai = LoaiSP.objects.all()
    data = {
        'DSLoai': listLoai,
        'DSSP': SanPham.objects.all(),
    }
    return render(request, 'pages/SanPham.html', data)

def DSSP_TheoLoai(request, id):
    # listLoai = LoaiSP.objects.all()
    dssp = SanPham.objects.all().filter(MaLoai= id)
    data = {
        # 'DSLoai': listLoai,
        'DSSP': dssp,
    }
    return render(request, 'pages/SanPham.html',data)

def chiTietSP(request, id):
    sp = SanPham.objects.get(id = id)
    ncc = NhaCungCap.objects.get(id = sp.MaNCC_id)
    data = {'SP': sp, 'NCC': ncc}
    return render (request, 'pages/ChiTietSP.html', data)
# lấy sản phẩm theo loại:

# ==================================================Các view cho quản lý=====================================
# sản phẩm hiển thị cho người quản lý
def DS_Loai_SP_1(request):
    listLoai = LoaiSP.objects.all()
    listSP =  SanPham.objects.all()
    paginator = Paginator(listSP,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {'DSLoai': listLoai, 'DSSP': page_obj,}
   
    return render(request, 'pages/SP_QL.html',data)
# Thêm sản phảm mới

def themSP(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES)
        if form.is_valid():
            san_pham = form.save(commit=False)
            if 'anh_tai_len' in request.FILES:
                anh_tai_len = request.FILES['anh_tai_len']
                anh_luu_duong_dan = os.path.join(settings.STATICFILES_DIRS[0], 'img', anh_tai_len.name)
                with open(anh_luu_duong_dan, 'wb+') as destination:
                    for chunk in anh_tai_len.chunks():
                        destination.write(chunk)
                san_pham.Anh = anh_tai_len.name
            san_pham.save()
            return redirect('/products/SPQL/')  
    else:
        form = SanPhamForm()
    return render(request, 'pages/ThemSP.html', {'form': form})
# xem trước khi xóa
    
def XemMoiXoa(request, id):
    sanpham = SanPham.objects.get(id=id)
    return render(request, 'pages/xemSP.html', {'sanpham': sanpham})
# xoá sp luôn
def XoaSP(request, id):
    sp = SanPham.objects.get(id = id)
    sp.delete()
    messages.success(request, 'Đã xóa sản phẩm thành công!!')
    return redirect('/products/SPQL') 
#Sửa sản phẩm. 
def updateSP(request, id):
    # san_pham = get_object_or_404(SanPham, id=id)
    
    # if request.method == 'POST':
    #     form = SanPhamForm(request.POST, request.FILES, instance=san_pham)
    #     if form.is_valid():
    #         san_pham = form.save(commit=False)
    #         if 'anh_tai_len' in request.FILES:
    #             anh_tai_len = request.FILES['anh_tai_len']
    #             anh_luu_duong_dan = os.path.join(settings.STATICFILES_DIRS[0], 'img', anh_tai_len.name)
    #             with open(anh_luu_duong_dan, 'wb+') as destination:
    #                 for chunk in anh_tai_len.chunks():
    #                     destination.write(chunk)
    #             san_pham.Anh = anh_tai_len.name
    #         san_pham.save()
    #         return redirect('/products/SPQL/')
    # else:
    #     form = SanPhamForm(instance=san_pham)
    # return render(request, 'pages/updateSP.html', {'form': form})

    san_pham = get_object_or_404(SanPham, id=id)
    
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES, instance=san_pham)
        if form.is_valid():
            san_pham = form.save(commit=False)
            if 'anh_tai_len' in request.FILES:
                anh_tai_len = request.FILES['anh_tai_len']
                anh_luu_duong_dan = os.path.join(settings.STATICFILES_DIRS[0], 'img', anh_tai_len.name)
                with open(anh_luu_duong_dan, 'wb+') as destination:
                    for chunk in anh_tai_len.chunks():
                        destination.write(chunk)
                san_pham.Anh = anh_tai_len.name
            san_pham.save()
            return redirect('/products/SPQL/')
    else:
        form = SanPhamForm(instance=san_pham)
    return render(request, 'pages/updateSP.html', {'form': form})

def ThemAnh(request):
    if request.method == 'POST':
        img = HinhAnh()
        if len(request.FILES) != 0 :
            img.img = request.FILES['img']  
        img.save()
        messages.success(request, 'Thêm thành công!!')
        return redirect('/')
    return render(request, 'pages/themAnh.html')
