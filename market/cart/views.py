from django.shortcuts import render, redirect
from django.views import generic, View
from core.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

class AddCartView(generic.ListView):
    template_name = 'product/checkout.html'
    model = Cart

    def post(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=request.POST['product_id'])
            user = User.objects.get(id=request.user.id)
            person = Person.objects.get(user_info=user)
            customer = Customer.objects.get(person_info=person)
            quantity = int(request.POST['quantity'])
            try:
                item_exists = Cart.objects.get(product_id=product, customer_id=customer)
                item_exists.quantity += 1
                item_exists.save()
            except ObjectDoesNotExist as e:
                items = Cart(product_id=product, customer_id=customer, price=product.price, quantity=quantity)
                items.save()
            user_cart = Cart.objects.filter(customer_id=customer)
            cart_list = []
            for item in user_cart:
                cart_list.append(item.product_id)
            # return render(request, self.template_name, {"cartList": cart_list})
            return redirect('/cart/', request)
        except ObjectDoesNotExist as e:
            return render(request, self.template_name, {"None": 1})


class CartView(generic.ListView):
    template_name = 'product/Cart.html'
    model = Cart


    def get(self, request, *args, **kwargs):
        '''
        Get method is used for redirect request from Add to cart View.
        '''
        try:
            user = User.objects.get(id=request.user.id)
            person = Person.objects.get(user_info=user)
            customer = Customer.objects.get(person_info=person)
            user_cart = Cart.objects.filter(customer_id=customer)
            return render(request, self.template_name, {"cartList": user_cart})
        except ObjectDoesNotExist as e:
            print(e)
            return render(request, self.template_name, {"None": 1})

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
            person = Person.objects.get(user_info=user)
            customer = Customer.objects.get(person_info=person)
            user_cart = Cart.objects.filter(customer_id=customer)
            return render(request, self.template_name, {"cartList": user_cart})
        except ObjectDoesNotExist as e:
            print(e)
            return render(request, self.template_name, {"None": 1})

class UpdateQuantityView(generic.edit.UpdateView):

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
            person = Person.objects.get(user_info=user)
            customer = Customer.objects.get(person_info=person)
            Cart.objects.filter(
                customer_id=customer, product_id=int(request.POST['product_id'])
            ).update(quantity=int(request.POST['quantity']))
            return HttpResponse("okay")
        except Exception as e:
            print(e)
            return HttpResponse("failed")


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
            user = User.objects.get(id=request.user.id)
            person = Person.objects.get(user_info=user)
            customer = Customer.objects.get(person_info=person)
            Cart.objects.filter(
                customer_id=customer, product_id=int(request.POST['product_id'])
            ).delete()
            return HttpResponse("okay")
        except Exception as e:
            print(e)
            return HttpResponse("failed")

