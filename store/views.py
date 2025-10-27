from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
from .models import Product
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProductsList(ListView, LoginRequiredMixin):
    model = Product
    template_name = "store/ProductList.html"


class AddToCartView(View):
    http_method_names = ["post"]
    
    def post(self, request, *args, **kwargs):
        # add products to the cart | stores them on the session
        product_id = str(self.kwargs.get('pk'))
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))

        # if the product exist in the cart, just increase the quantity
        if product_id in cart:
            cart[product_id] += quantity
        else:
            # new product, add it
            cart[product_id] = quantity

        # put the cart in the session
        request.session['cart'] = cart
        return HttpResponseRedirect(reverse('products_list'))


class CartListView(View):

    def get(self, request, *arg, **kwargs):
        cart = request.session.get('cart', {})
        print("got from session", cart)
        cart_items = {}

        for product_id, quantity in cart.items():
            # read the product using product_id
            product = Product.objects.get(pk=product_id)
            cart_items[product] = quantity

        return render(request, 'store/cart.html', {'cart': cart_items})


class RemoveFromCartView(View):
    def post(self, request, pk, *args, **kwargs):
        cart = request.session.get('cart', {})
        print("deleting", cart)
        if pk in cart:
            del cart[pk]
            request.session['cart'] = cart

        return HttpResponseRedirect(reverse('cart'))