from django.shortcuts import render, redirect
from django.http import JsonResponse
from cart.models import Cart
from products.models import SanPham
from account.models import KhachHang, HoaDon, ChiTietHD
from django.db.models import Sum
from datetime import datetime

def view_cart(request):
    username = request.session['username']
    cart = Cart.objects.filter(UserName__UserName=username)
    data = {
        'cart': cart,
    }
    return render(request, 'shop-cart/cart.html', data)

def add_to_cart(request):
    if request.method == "POST":
        try:
            product_id = int(request.POST.get('product_id'))
            product = SanPham.objects.get(id = product_id)
            username = request.session['username']
            khachHang = KhachHang.objects.get(UserName=username)
            if 'username' not in request.session:
                return JsonResponse({'error': f"{username} not logged in"}, status=400)
            else:
                soLuong = int(request.POST.get('quantity'))
                thanhTien = soLuong * product.GiaBan
                cart = Cart.objects.filter(UserName=khachHang, ProductId=product).first()
                if not cart:
                    cart = Cart(
                            ProductId = product,
                            UserName = khachHang,
                            SoLuong = soLuong,
                            ThanhTien = thanhTien,
                        )
                    # return JsonResponse({'success': f"Product added {cart.SoLuong} to cart - {soLuong}*{product.GiaBan}={thanhTien}"})
                    cart.save()
                # if cart:
                else:
                    soLuongDB = cart.SoLuong
                    SL = soLuongDB + soLuong
                    cart.SoLuong = SL
                    cart.ThanhTien = SL * product.GiaBan
                    cart.save()
                return JsonResponse({'success': 'Product added to cart'})
        except SanPham.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def remove_from_cart(request, id):
    product = SanPham.objects.get(id = id)
    username = request.session['username']
    khachHang = KhachHang.objects.get(UserName=username)

    Cart.objects.filter(UserName=khachHang, ProductId=product).delete()
    return redirect('view_cart')


def checkout(request):
    # Kiểm tra xem phiên có tồn tại và lấy tên người dùng từ phiên
    if 'username' in request.session:
        username = request.session['username']
        
        khachHang = KhachHang.objects.get(UserName=username)

        # Lấy tổng của tất cả các giá trị ThanhTien trong bảng Cart dựa trên UserName
        total = Cart.objects.filter(UserName__UserName=username).aggregate(Sum('ThanhTien'))['ThanhTien__sum']
        
        # Lấy tất cả các ProductId từ các đối tượng Cart
        product_ids_in_cart = Cart.objects.values_list('ProductId', flat=True)
        cart = Cart.objects.filter(UserName__UserName=username)

        # Lấy tất cả các sản phẩm từ bảng SanPham có ProductId nằm trong danh sách product_ids_in_cart
        products_in_cart = SanPham.objects.filter(id__in=product_ids_in_cart)

        # Nếu không có giá trị nào, tổng sẽ là 0
        if total is None:
            total = 0
    else:
        # Nếu không có phiên hoặc không có tên người dùng trong phiên, gán tổng là 0
        total = 0

    data = {
        'kh' : khachHang,
        'total': total, 
        'products': products_in_cart,
        'cart': cart
    }
    
    return render(request, 'shop-cart/checkout.html', data)


def process_order(request):
    username = request.session['username']
    # user = Account.objects.filter(UserName=username).first()
    khachHang = KhachHang.objects.get(UserName=username)

    if request.method == 'POST':
        # Lấy dữ liệu từ request.POST
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        shipping_method = request.POST.get('shipping_method')
        payment_method = request.POST.get('payment_method')
        total = request.POST.get('total')

        hoaDon = HoaDon.objects.create(
            MaKH=khachHang,
            NgayLap=datetime.now(),
            TongTien=total,
            PhuongThucVanChuyen=shipping_method,
            PhiVanChuyen=0,
            PhuongThucThanhToan=payment_method,
            GhiChu="",
            TrangThai='pending',
        )
        hoaDon.save()

        cart_items = Cart.objects.filter(UserName=khachHang)
        for item in cart_items:
            chiTietHoaDon = ChiTietHD.objects.create(
                MaHD = hoaDon,
                MaSP = item.ProductId,
                SoLuong = item.SoLuong,
                ThanhTien = item.ThanhTien,
            )
            chiTietHoaDon.save()

        # xóa thông tin giỏ hàng của session user này
        cart_items.delete()

        return redirect('receipt')  
    return redirect('checkout')  

