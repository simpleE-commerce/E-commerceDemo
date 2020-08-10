from django.shortcuts import render
from django.views import generic, View
from core.models import *
from django.core.exceptions import ObjectDoesNotExist

class AddCartView(generic.ListView):
    template_name = 'product/checkout.html'
    model = Cart

    def post(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=request.POST['product_id'])
            print(product,"**************************************")
            user = User.objects.get(id=request.user.id)
            print(user, "###########################################33")
            person = Person.objects.get(user_info=user)
            print(person, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            customer = Customer.objects.get(person_info=person)
            print(customer, "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            quantity = int(request.POST['quantity'])
            try:
                item_exists = Cart.objects.get(product_id=product, customer_id=customer)
                item_exists.quantity += 1
                item_exists.save()
            except ObjectDoesNotExist as e:
                items = Cart(product_id=product, customer_id=customer, price=product.price, quantity=quantity)
                items.save()
            print("qu", quantity)
            user_cart = Cart.objects.filter(customer_id=customer)
            print('c', user_cart)
            cart_list = []
            for item in user_cart:
                # temp_list = [item.product_id, item.quantity]
                cart_list.append(item.product_id)
            print(cart_list)
            return render(request, self.template_name, {"cartList": cart_list})
        except ObjectDoesNotExist as e:
            print(e)
            return render(request, self.template_name, {"None": 1})


class CartView(generic.ListView):
    template_name = 'product/checkout.html'
    model = Cart

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
            print(user, "###########################################33")
            person = Person.objects.get(user_info=user)
            print(person, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            customer = Customer.objects.get(person_info=person)
            print(customer, "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            user_cart = Cart.objects.filter(customer_id=customer)
            print('c', user_cart)
            cart_list = []
            for item in user_cart:
                # temp_list = [item.product_id, item.quantity]
                cart_list.append(item.product_id)
            print(cart_list)
            return render(request, self.template_name, {"cartList": user_cart})
        except ObjectDoesNotExist as e:
            print(e)
            return render(request, self.template_name, {"None": 1})



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
            if total_price - discount_amount == request.POST['amount']:
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

