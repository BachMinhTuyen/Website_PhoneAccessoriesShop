from django.shortcuts import render
from django.http import HttpResponse

from products.models import LoaiSP, SanPham
#Create your views here.
def index(request):
    data = {
        'DanhSachLoai' : LoaiSP.objects.all(),
        'DanhSachSanPham' : SanPham.objects.all(),
    }
    return render(request, 'page/home.html', data)

def aboutus(request):
    return render(request, 'page/aboutUs.html')

def contact(request):
    return render(request, 'page/contact.html')

