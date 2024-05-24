from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account, KhachHang, NhanVien

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
    
    if status == 'processing':
        return render(request, 'page/receiptProcessing.html')
    elif status == 'completed':
        return render(request, 'page/receiptCompleted.html')
    elif status == 'cancel':
        return render(request, 'page/receiptCancel.html')
    else:
        return render(request, 'page/receipt.html')

def receiptdetails(request):
    return render(request, 'page/receiptdetails.html')