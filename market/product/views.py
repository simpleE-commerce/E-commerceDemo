from django.shortcuts import render
from django.views import generic
from core.models import *
from django.http import HttpResponse


class ProductsListClassView(generic.ListView):
    template_name = 'product/product.html'
    model = Product
    context_object_name = 'products'


class SearchView(generic.ListView):
    template_name = 'product/product.html'
    model = Product
    
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(product_name__icontains=request.GET['term'])
        return render(request, self.template_name, {"products": products})


# class ProductDetails(generic.TemplateView):
#     template_name = 'product/single.html'


class ProductDetailClassView(generic.DetailView):
    model = Product
    template_name = 'product/single.html'

    def get_context_data(self, **kwargs):
        print(kwargs['object'].id)
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.get(id=kwargs['object'].id)
        context['images'] = ProductImage.objects.filter(product_id=kwargs['object'].id)
        context['description'] = ProductDetails.objects.filter(product_id=kwargs['object'].id)
        return context

class CheckoutListView(generic.ListView):
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
            return render(request, self.template_name, {"cartList": cart_list})
        except ObjectDoesNotExist as e:
            print(e)
            return render(request, self.template_name, {"None": 1})