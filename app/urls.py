from django.conf import settings
from django.templatetags.static import static
from django.urls import path
from .views import SHop, ShopDetail, Contact, Cart, Testimonial, Eror404, Checkout, Products, Register

urlpatterns = [
    path('', Products.as_view(), name='home'),
    path('shop/', SHop.as_view(), name='shop'),
    path('shop-detail/', ShopDetail.as_view(), name='shop_detail'),
    path('contact/', Contact.as_view(), name='contact'),
    path('cart/', Cart.as_view(), name='cart'),
    path('404/', Eror404.as_view(), name='404'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('register/', Register.as_view(), name='register'),
]

