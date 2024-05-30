from django import forms
from .models import KhachHang

class ProfileForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Họ và tên')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=100, label='Số điện thoại')
    address = forms.CharField(max_length=100, label='Địa chỉ')

    def update_profile(self, username):
        cleaned_data = self.cleaned_data
        KhachHang.objects.filter(UserName=username).update(
            TenKH=cleaned_data['full_name'],
            Email=cleaned_data['email'],
            SoDT=cleaned_data['phone_number'],
            DiaChi=cleaned_data['address'],
        )    