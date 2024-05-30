from django import forms
from account.models import KhachHang, Account

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

class SignInForm(forms.Form):

    current_password = forms.CharField(max_length=100, label='Mật khẩu hiện tại')
    new_password = forms.CharField(max_length=100, label='Mật khẩu mới')
    confirm_password = forms.CharField(max_length=100, label='Nhập lại mật khẩu mới')

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp.")
        return cleaned_data
    
    def update_password(self, username):
        cleaned_data = self.cleaned_data
        acc = Account.objects.filter(UserName=username).first()
        
        if acc and acc.Password == cleaned_data['current_password']:
            acc.Password = cleaned_data['new_password']
            acc.save()
            return True
        else:
            raise forms.ValidationError(f"{acc.Password} - Mật khẩu hiện tại không đúng.")
