from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from account.models import ChiTietHD, HoaDon, KhachHang, NhanVien
from dashboard.forms import ChiTietPhieuNhapForm, ChiTietPhieuNhapFormSet, PhieuNhapForm, SuaSanPhamForm, TheLoaiForm, NhaCungCapForm, ThemSanPhamForm
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
            san_pham = form.save(commit=False)
            san_pham.Soluong = 0  
            san_pham.GiaNhap = 0
            san_pham.TrangThai =False
            san_pham.GiaBan = 0
            san_pham.save()
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
        form = SuaSanPhamForm(request.POST, instance=sanpham)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect('/dashboard/SanPham')
    else:
        form = SuaSanPhamForm(instance=sanpham)

    return render(request, 'page/Sua_SP.html', {'form': form, 'sanpham': sanpham})

def XemCT_SP(request, sp_id):
    sp = SanPham.objects.get(id=sp_id)
    data = {
        'single_product': sp,
    }
    return render(request, 'page/XemCT_SP.html', data)

#HoaDon
def list_HoaDon(request):
    # invoices = HoaDon.objects.filter(MaKH=khachHang)
    chiTietHD = ChiTietHD.objects.all()
    invoices = HoaDon.objects.all()
    data = {
        'hoaDonLST': invoices,
        'chiTietHD': chiTietHD,
    }
    return render(request, 'page/HoaDon.html', data)



def receiptdetails(request, MaHD):
    # username = request.session['username']
    # khachHang = KhachHang.objects.get(UserName=username)
    hoaDon = HoaDon.objects.filter(MaHD=MaHD).first()
    chiTietHD = ChiTietHD.objects.filter(MaHD=hoaDon)
    data = {
        'hoaDon' : hoaDon,
        'chiTietHD' : chiTietHD,
    }
    return render(request, 'page/XemCT_HD.html', data)


def cancelOrder(request, MaHD):
    hoaDon = HoaDon.objects.filter(MaHD=MaHD).first()
    hoaDon.TrangThai='cancel'
    hoaDon.save()
    return redirect('HoaDon')




def ConfirmOrder(request, MaHD):
    hoaDon = HoaDon.objects.filter(MaHD=MaHD).first()
    hoaDon.TrangThai='processing'
    hoaDon.save()
    return redirect('HoaDon')


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
            phieunhap.save()  

            for form in formset:
                if form.cleaned_data:
                    quantity = form.cleaned_data.get('SoLuong', 0)
                    price = form.cleaned_data.get('GiaNhap', 0)
                    san_pham = form.cleaned_data.get('MaSP')
                    if san_pham:
                        san_pham.Soluong += quantity
                        san_pham.GiaNhap = price 
                        san_pham.TrangThai =True
                        san_pham.save()

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

#xem chi tiết phiếu nhập 
def XemCTPN(request, MaPhieuNhap):
    pn = ChiTietPhieuNhap.objects.filter( MaPhieuNhap=MaPhieuNhap)
    data = {
        'DM_XemCTPN': pn,
    }
    return render(request, 'page/XemCTPN.html', data)

#xóa phiếu nhập
def Xoa_PN(request, id):
    pn = PhieuNhap.objects.get(id=id)
    pn.delete()
    return HttpResponseRedirect('/dashboard/Phieu_Nhap')

    
    
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
