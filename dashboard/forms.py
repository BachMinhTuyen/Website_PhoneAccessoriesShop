from django import forms
from account.models import NhanVien
from products.models import NhaCungCap,LoaiSP,SanPham
from .models import PhieuNhap, ChiTietPhieuNhap
from django.forms import inlineformset_factory

#Them Loai
class TheLoaiForm(forms.ModelForm):
    class Meta:
        model = LoaiSP
        fields = ['TenLoai']
        widgets = {
            'TenLoai': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_TenLoai(self):
        TenLoai = self.cleaned_data['TenLoai']

        try:
            LoaiSP.objects.get(TenLoai=TenLoai)
        except LoaiSP.DoesNotExist:
            return TenLoai
        raise forms.ValidationError("Loại sản phẩm đã tồn tại")

#Them NCC
class NhaCungCapForm(forms.ModelForm):
    class Meta:
        model = NhaCungCap
        fields = '__all__'
        widgets = {
            'TenNCC': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_TenNCC(self):
        TenNCC = self.cleaned_data['TenNCC']

        try:
            NhaCungCap.objects.get(TenNCC=TenNCC)
            raise forms.ValidationError("Tên nhà cung cấp đã tồn tại.")
        except NhaCungCap.DoesNotExist:
            return TenNCC


            
        
class ThemSanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['TenSP', 'MaLoai', 'MaNCC', 'Mota', 'Anh', 'TenThietBi']

            
        
class SuaSanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['TenSP', 'MaLoai', 'MaNCC', 'Mota', 'Anh', 'TenThietBi','Soluong','GiaNhap','GiaBan']      
    
       
        
        
# Lap Phieu Nhap Hang
class PhieuNhapForm(forms.ModelForm):
    NgayNhap = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-input','type': 'date'}))
    TrangThai = forms.BooleanField(required=True) 
    class Meta:
        model = PhieuNhap
        fields = ['MaNV', 'NgayNhap', 'TongTien','TrangThai']
        
    def __init__(self, *args, **kwargs):
        super(PhieuNhapForm, self).__init__(*args, **kwargs)
        self.fields['TongTien'].widget.attrs['readonly'] = True

class ChiTietPhieuNhapForm(forms.ModelForm):
    class Meta:
        model = ChiTietPhieuNhap
        fields = ['MaSP', 'MaNCC', 'SoLuong', 'GiaNhap']


ChiTietPhieuNhapFormSet = inlineformset_factory(
    PhieuNhap, ChiTietPhieuNhap, form=ChiTietPhieuNhapForm, extra=1, can_delete=True
)
