from django.urls import path
from django.conf.urls.static import static
from phoneaccessorieswebsite_django import settings
from . import views # call to url_shortener/views.py
app_name = 'products'
if settings.DEBUG:
    urlpatterns = [
        path('', views.DSSP, name='DMSP'),
        # path('thongtin/', views.index, name='index'),
        path('detail/<int:id>/', views.chiTietSP),
        path('producttype/<int:id>/', views.DSSP_TheoLoai, name='SPLoai'),

        path('themSP/', views.themSP, name= 'ThemSP'),
        path('SPQL/', views.DS_Loai_SP_1, name= 'SPQL'),
        path('xemSP/<int:id>/', views.XemMoiXoa, name= 'xemsp'),
        path('xoaSP/<int:id>/', views.XoaSP, name= 'xoasp'),
        path('updateSP/<int:id>/', views.updateSP, name='updateSP'),
        path('themAnh/', views.ThemAnh, name= 'ThemAnh'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)