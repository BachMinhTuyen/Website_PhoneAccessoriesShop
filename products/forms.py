from django import forms
from .models import SanPham,LoaiSP
from products.models import NhaCungCap
class SanPhamForm(forms.ModelForm):
    anh_tai_len = forms.ImageField(required=False)
    MaNCC = forms.ModelChoiceField(
        queryset=NhaCungCap.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Nhà cung cấp"
    )

    MaLoai = forms.ModelChoiceField(
        queryset=LoaiSP.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Loại sản phẩm"
    )

    class Meta:
        model = SanPham
        fields = ['TenSP', 'Soluong', 'GiaNhap', 'GiaBan', 'MaLoai', 'MaNCC', 'Mota', 'TrangThai', 'TenThietBi', 'anh_tai_len']
        widgets = {
            'TenSP': forms.TextInput(attrs={'class': 'form-control'}),
            'Soluong': forms.NumberInput(attrs={'class': 'form-control'}),
            'GiaNhap': forms.NumberInput(attrs={'class': 'form-control'}),
            'GiaBan': forms.NumberInput(attrs={'class': 'form-control'}),
            'MaLoai': forms.Select(attrs={'class': 'form-control'}),
            'MaNCC': forms.Select(attrs={'class': 'form-control'}),
            'Mota': forms.Textarea(attrs={'class': 'form-control'}),
            'TrangThai': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'TenThietBi': forms.TextInput(attrs={'class': 'form-control'}),
            'anh_tai_len': forms.FileInput(attrs={'class': 'mt-3 btn btn-primary', 'style': 'display: inline-block;'})
        }

    def save(self, commit=True):
        instance = super(SanPhamForm, self).save(commit=False)
        if self.cleaned_data.get('anh_tai_len'):
            instance.Anh = self.cleaned_data.get('anh_tai_len').name
        if commit:
            instance.save()
        return instance
