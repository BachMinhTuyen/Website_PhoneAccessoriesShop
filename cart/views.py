from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Order

def index(request):
    products = Product.objects.all()
    return render(request, 'shop-cart/index.html', {'products': products})

def view_cart(request):
    cart = Cart.objects.all()
    return render(request, 'shop-cart/cart.html', {'cart': cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(Cart, product_id=product_id)
    cart_item.delete()
    return redirect('view_cart')

def checkout(request):
    cart = Cart.objects.all()
    total = sum(item.product.price * item.quantity for item in cart)
    return render(request, 'shop-cart/checkout.html', {'cart': cart, 'total': total})

def process_order(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        shipping_method = request.POST.get('shipping_method')
        payment_method = request.POST.get('payment_method')

        # Tạo đơn hàng mới
        order = Order.objects.create(
            full_name=full_name,
            address=address,
            phone=phone,
            email=email,
            shipping_method=shipping_method,
            payment_method=payment_method
        )

        # Lưu các sản phẩm từ giỏ hàng vào đơn hàng
        cart_items = Cart.objects.all()
        for item in cart_items:
            order.order_items.create(
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Xóa giỏ hàng sau khi đã đặt hàng
        Cart.objects.all().delete()

        # Hiển thị thông báo thành công
        messages.success(request, 'Đơn hàng đã được đặt thành công!')

        # Chuyển hướng người dùng đến trang cảm ơn hoặc trang chủ
        return redirect('thank_you_page')  # Thay 'thank_you_page' bằng tên đường dẫn tới trang cảm ơn

    # Nếu không phải phương thức POST, chuyển hướng về trang checkout
    return redirect('checkout')

