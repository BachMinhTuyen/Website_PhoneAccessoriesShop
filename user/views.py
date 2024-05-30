from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import Account, KhachHang, NhanVien, HoaDon, ChiTietHD
from products.models import SanPham
from cart.models import Cart
from user.forms import ProfileForm, SignInForm

# Create your views here.
def profile(request):
    username = request.session['username']
    user = Account.objects.filter(UserName=username).first()
    if (user.Quyen == 'khachhang'):
        taiKhoan = Account.objects.get(UserName=username)
        khachHang = KhachHang.objects.get(UserName=username)
        data = {
            'acc' : taiKhoan,
            'kh' : khachHang,
        }
        return render(request, 'page/profile.html', data)
    if (user.Quyen == 'nhanvien'):
        taiKhoan = Account.objects.get(UserName=username)
        nhanVien = NhanVien.objects.get(UserName=username)
        data = {
            'acc' : taiKhoan,
            'kh' : nhanVien,
        }
        return render(request, 'page/profile.html', data)

def receipt(request):
    status = request.GET.get('status')

    username = request.session['username']
    khachHang = KhachHang.objects.get(UserName=username)
    invoices = HoaDon.objects.filter(MaKH=khachHang)
    chiTietHD = ChiTietHD.objects.all()
    
    if status == 'processing':
        return render(request, 'page/receiptProcessing.html')
    elif status == 'completed':
        return render(request, 'page/receiptCompleted.html')
    elif status == 'cancel':
        return render(request, 'page/receiptCancel.html')
    else:
        data = {
            'hoaDonLST': invoices,
            'chiTietHD': chiTietHD,
        }
        return render(request, 'page/receipt.html', data)

def receiptdetails(request, MaHD):
    # username = request.session['username']
    # khachHang = KhachHang.objects.get(UserName=username)
    hoaDon = HoaDon.objects.filter(MaHD=MaHD).first()
    chiTietHD = ChiTietHD.objects.filter(MaHD=hoaDon)
    data = {
        'hoaDon' : hoaDon,
        'chiTietHD' : chiTietHD,
    }
    return render(request, 'page/receiptdetails.html', data)

def updateProfile(request):
    if 'username' not in request.session:
        return redirect('user_login')
    
    username = request.session['username']

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.update_profile(username)
            return redirect('profile')
        
def updatePassword(request):
    if 'username' not in request.session:
        return redirect('user_login')
    
    username = request.session['username']

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.update_password(username)
            return redirect('profile')