from django.shortcuts import render
from django.views import generic, View
from core.models import *
from django.core.exceptions import ObjectDoesNotExist

class AddCartView(View):

    def post(self, request, *args, **kwargs):
        try:
            product_id = request.POST['product_id']
            customer_id = request.user.id
            quantity = request.POST['quantity']
            price = Product.objects.get(id=product_id).price
            items = Cart(product_id=product_id, customer_id=customer_id, price=price, quantity=quantity)
            items.save()
        except ObjectDoesNotExist as e:
            print(e)


class CartView(generic.ListView):
    template_name = 'cart/cartlist.html'
    model = Cart

    def post(self, request, *args, **kwargs):
        customer_id = request.user.id
        items_in_cart = Cart.objects.filter(customer_id=customer_id)
        return render(request, self.template_name, {"items": items_in_cart})


class CheckOutView(View):
    
    def post(self, request, *args, **kwargs):
        if request.POST['result']:
            customer_id = request.user.id
            total_price = 00.2
            discount_amount = ''
            order = Orders(customer_id=customer_id, 
                           seller_id=request.POST['seller_id'],
                           total_price=total_price,
                           discount_amount=discount_amount)
            order.save()
            product_price = Product.objects.get(id=request.POST['product_id']).price
            order_list = OrderList(order_id=order.id,
                                   product_id=request.POST['product_id'],
                                   price=product_price,
                                   quantity=request.POST['quantity'])
            order_list.save()
            if total_price - discount_amount == request.POST['amount']
                payment = Payments(order_id=order.id,
                                    amount=request.POST['amount'],
                                    status=2)
            else:
                payment = Payments(order_id=order.id,
                                    amount=request.POST['amount'],
                                    status=2)
            payment.save()
            Cart.objects.filter(customer_id=customer_id).delete()


class DeleteItemCart(View):

    def post(self, request, *args, **kwargs):
        try:
            product_id = request.POST['product_id']
            customer_id = request.user.id
            Cart.objects.filter(product_id=product_id, customer_id=customer_id).delete()
        except ObjectDoesNotExist as e:
            print(e)

