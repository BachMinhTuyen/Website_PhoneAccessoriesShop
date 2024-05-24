from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from account.models import HoaDon, KhachHang, NhanVien
from dashboard.forms import ChiTietPhieuNhapForm, ChiTietPhieuNhapFormSet, PhieuNhapForm, TheLoaiForm, NhaCungCapForm, ThemSanPhamForm
from dashboard.models import PhieuNhap,ChiTietPhieuNhap
from products.models import NhaCungCap, LoaiSP, SanPham
from django.forms.models import inlineformset_factory



def index(request):
    return render(request, 'page/dashboard.html') 

#Loại Sản Phẩm
def list_LoaiSP(request):
   data = {
   'DM_LoaiSP': LoaiSP.objects.all(), 
   }
   return render(request, 'page/LoaiSP.html', data)

def Them_LoaiSP(request):
   form = TheLoaiForm()
   if request.method == 'POST':
      form = TheLoaiForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/dashboard/LoaiSP')
   return render(request,'page/Them_LoaiSP.html',{'form':form})

def Xoa_LoaiSP(request, loai_id):
    loai_sp = LoaiSP.objects.get(id=loai_id)
    loai_sp.delete() 
    return HttpResponseRedirect('/dashboard/LoaiSP')  

def Sua_LoaiSP(request, loai_id):
    loai_sp = LoaiSP.objects.get(id=loai_id)
    if request.method == 'POST':
        form = TheLoaiForm(request.POST, instance=loai_sp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/LoaiSP')
    else:
        form = TheLoaiForm(instance=loai_sp)

    return render(request, 'page/Sua_LoaiSP.html', {'form': form, 'loai_sp': loai_sp})


#Nhà Cung Cấp
def list_NhaCungCap(request):
   data = {
   'DM_NCC': NhaCungCap.objects.all(), 
   }
   return render(request, 'page/NhaCungCap.html', data)


def Them_NCC(request):
    if request.method == 'POST':
        form = NhaCungCapForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/dashboard/NhaCungCap')  
    else:
        form = NhaCungCapForm()

    context = {'form': form}
    return render(request, 'page/Them_NCC.html', context)


def Xoa_NCC(request, ncc_id):
    loai_NCC = NhaCungCap.objects.get(id=ncc_id)
    loai_NCC.delete() 
    return HttpResponseRedirect('/dashboard/NhaCungCap') 


def Sua_NCC(request, ncc_id):
    ncc = NhaCungCap.objects.get(id=ncc_id)
    if request.method == 'POST':
        form = NhaCungCapForm(request.POST, instance=ncc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/NhaCungCap')
    else:
        form = NhaCungCapForm(instance=ncc)

    return render(request, 'page/Sua_NCC.html', {'form': form, 'ncc': ncc})


#Sản Phẩm
def list_SanPham(request):
   data = {
   'DM_SP': SanPham.objects.all(), 
   }
   return render(request, 'page/SanPham.html', data)


def Them_SanPham(request):
    if request.method == 'POST':
        form = ThemSanPhamForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/dashboard/SanPham')  
    else:
        form = ThemSanPhamForm()

    context = {'form': form}
    return render(request, 'page/Them_SanPham.html', context)


def Xoa_SP(request, sp_id):
    sanpham = SanPham.objects.get(id=sp_id)
    sanpham.delete()
    return HttpResponseRedirect('/dashboard/SanPham')

def Sua_SP(request, sp_id):
    sanpham = SanPham.objects.get(id=sp_id)
    if request.method == 'POST':
        form = ThemSanPhamForm(request.POST, instance=sanpham)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/SanPham')
    else:
        form = ThemSanPhamForm(instance=sanpham)

    return render(request, 'page/Sua_SP.html', {'form': form, 'sanpham': sanpham})


def XemCT_SP(request, sp_id):
    sp = SanPham.objects.get(id=sp_id)
    data = {
        'single_product': sp,
    }
    return render(request, 'page/XemCT_SP.html', data)

#HoaDon
def list_HoaDon(request):
    data = {
        'DM_HD':HoaDon.objects.all(),
    }
    return render(request, 'page/HoaDon.html', data)


def XemCT_HD(request, MaHD):
    data = {
        'DM_XemCT_HD': HoaDon.objects.get(MaHD=MaHD),
    }
    return render(request, 'page/XemCT_HD.html', data)


#Phiếu nhập
def list_PhieuNhap(request):
    data = {
        'DM_PhieuNhap': PhieuNhap.objects.all(),
    }
    return render(request, 'page/Phieu_Nhap.html', data)


def LapPhieuNhap(request):
    if request.method == 'POST':
        phieunhap_form = PhieuNhapForm(request.POST)
        formset = ChiTietPhieuNhapFormSet(request.POST, instance=phieunhap_form.instance)
        
        if phieunhap_form.is_valid() and formset.is_valid():
            phieunhap = phieunhap_form.save(commit=False)
            total_amount = 0
            for form in formset:
                if form.cleaned_data:
                    quantity = form.cleaned_data.get('SoLuong', 0)
                    price = form.cleaned_data.get('GiaNhap', 0)
                    total_amount += quantity * price
            phieunhap.TongTien = total_amount
            phieunhap.save()
            formset.instance = phieunhap
            formset.save()
            return HttpResponseRedirect('/dashboard/Phieu_Nhap') 
    else:
        phieunhap_form = PhieuNhapForm()
        formset = ChiTietPhieuNhapFormSet(instance=PhieuNhap())

    return render(request, 'page/LapPhieuNhap.html', {
        'phieunhap_form': phieunhap_form,
        'formset': formset,
    })
# def Sua_PN(request, pk):
#     phieunhap = get_object_or_404(PhieuNhap, pk=pk)
#     if request.method == 'POST':
#         phieunhap_form = PhieuNhapForm(request.POST, instance=phieunhap)
#         formset = ChiTietPhieuNhapFormSet(request.POST, instance=phieunhap)
        
#         if phieunhap_form.is_valid() and formset.is_valid():
#             phieunhap = phieunhap_form.save(commit=False)
#             total_amount = 0
#             for form in formset:
#                 if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
#                     quantity = form.cleaned_data.get('SoLuong', 0)
#                     price = form.cleaned_data.get('GiaNhap', 0)
#                     total_amount += quantity * price
#             phieunhap.TongTien = total_amount
#             phieunhap.save()
#             formset.instance = phieunhap
#             formset.save()
#             return HttpResponseRedirect('/dashboard/PhieuNhap')  
#     else:
#         phieunhap_form = PhieuNhapForm(instance=phieunhap)
#         formset = ChiTietPhieuNhapFormSet(instance=phieunhap)

#     return render(request, 'page/Sua_PN.html', {
#         'phieunhap_form': phieunhap_form,
#         'formset': formset,
#     })
    
    

def XemCT_PN(request, MaPN):
    data = {
        'DM_CTPN': ChiTietPhieuNhap.objects.get(MaPN=MaPN),
    }
    return render(request, 'page/XemCT_PN.html', data)

#Nhan Vien
def list_NhanVien(request):
    data = {
        'DM_NhanVien': NhanVien.objects.all(),
    }
    return render(request, 'page/NhanVien.html', data)

#KhachHang
def list_KhachHang(request):
    data = {
        'DM_KhachHang': KhachHang.objects.all(),
    }
    return render(request, 'page/KhachHang.html', data)
