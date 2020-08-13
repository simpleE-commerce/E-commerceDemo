from django.shortcuts import render, redirect
from django.views import generic, View
from core.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


class AddCartView(generic.ListView):
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
            return redirect('/cart/', request)
        except (ObjectDoesNotExist, Exception) as e:
            if not request.user.is_authenticated:
                print("not auth")
                return redirect('/login/')


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


class CheckOutView(generic.edit.CreateView):   
    
    def post(self, request, *args, **kwargs):
        try:
            product_list = [int(x) for x in request.POST.getlist("product_id[]")]
            user = User.objects.get(id=request.user.id)
            person = Person.objects.get(user_info=user)
            customer = Customer.objects.get(person_info=person)
            total_price = 0
            discount_amount = 0
            for ids in product_list:
                total_price += Product.objects.get(id=ids).price
            seller = Seller.objects.get(
                seller_info=Person.objects.get(
                    user_info=User.objects.get(username='admin')
                )
            )
            order = Orders(customer_id=customer, 
                           seller_id=seller,
                           total_price=total_price,
                           discount_amount=discount_amount)
            order.save()
            for ids in product_list:
                item = Product.objects.get(id=ids)
                quantity = Cart.objects.get(customer_id=customer, product_id=item).quantity
                order_list = OrderList(order_id=order,
                                        product_id=item,
                                        price=item.price,
                                        quantity=quantity)
                order_list.save()

            payment = Payments(order_id=order,
                                amount=total_price,
                                status=2)
            payment.save()
            Cart.objects.filter(customer_id=customer).delete()
            return HttpResponse("Okay")
        except Exception as e:
            print(e)
            return HttpResponse("Failed")


class DeleteItemCart(generic.edit.DeleteView):

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

