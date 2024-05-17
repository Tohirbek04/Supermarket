from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from app.models import Product, Categories, Base


class Products(View):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        fruits = Product.objects.filter(category__slug='fruit')
        vegetables = Product.objects.filter(category__slug='vegetable')
        breads = Product.objects.filter(category__slug='bread')
        meats = Product.objects.filter(category__slug='meat')

        context = {
            "products": products,
            "fruits": fruits,
            "vegetables": vegetables,
            "breads": breads,
            "meats": meats,
        }
        return render(self.request, 'index.html', context)


class SHop(TemplateView):
    template_name = 'shop.html'


class ShopDetail(TemplateView):
    template_name = 'shop-detail.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class Cart(TemplateView):
    template_name = 'cart.html'


class Eror404(TemplateView):
    template_name = '404.html'


class Testimonial(TemplateView):
    template_name = 'testimonial.html'


class Checkout(TemplateView):
    template_name = 'chackout.html'


class Register(TemplateView):
    template_name = 'login_register.html'
