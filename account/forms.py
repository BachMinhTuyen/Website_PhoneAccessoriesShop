from django import forms
from .models import Account, KhachHang

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Mật khẩu', widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, label='Nhập lại mật khẩu', widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=100, label='Họ và tên')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=100, label='Số điện thoại')
    address = forms.CharField(max_length=100, label='Địa chỉ')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp.")
        
        return cleaned_data

    def save(self):
        cleaned_data = self.cleaned_data
        account = Account.objects.create(
            UserName=cleaned_data['username'],
            Password=cleaned_data['password'],
            Quyen='khachhang'
        )
        KhachHang.objects.create(
            UserName=account,
            TenKH=cleaned_data['full_name'],
            Email=cleaned_data['email'],
            SoDT=cleaned_data['phone_number'],
            DiaChi=cleaned_data['address']
        )
        return account