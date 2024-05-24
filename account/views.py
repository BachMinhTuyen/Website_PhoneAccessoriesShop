from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Account, KhachHang

# Create your views here.
def user_login(request):
    # if (request.session["username"]):
    #     return redirect('profile')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Account.objects.filter(UserName=username, Password=password).first()
        if (user):
            request.session["username"] = user.UserName
            if (user.Quyen == 'khachhang'):
                # login(request, user)
                # request.session["username"] = user.UserName
                return redirect('home')
            if (user.Quyen == 'nhanvien'):
                return redirect('dashboard')
        else:
            messages.error(request, 'Thông tin đăng nhập không chính xác.')
    return render(request, 'page/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = RegistrationForm()

    data = {
        'form': form,
    }
    return render(request, 'page/register.html', data)

def logout(request):
    try:
        # request.session.flush()
        del request.session["username"]
    except KeyError:
        pass
    return redirect('user_login')