# from cart.models import Cart
# from account.models import KhachHang

# def cart_badge(request):
#     if (request.session['username']):
#         username = request.session['username']
#         khachHang = KhachHang.objects.get(UserName=username)

#         unique_product_count = 0
#         unique_product_count = Cart.objects.filter(UserName=khachHang).values('ProductId').distinct().count()
        
#         data = {
#             'unique_product_count':unique_product_count,
#         }
#         return data
#     return 0