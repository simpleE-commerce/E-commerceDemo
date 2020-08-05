from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    phone_number = models.CharField(max_length=13, blank=False)
    address = models.CharField(max_length=50, blank=False)


class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=15, blank=False)
    price = models.FloatField()
    available = models.BooleanField()
    inventory_count = models.IntegerField()


class ProductDetails(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=20, blank=False)
    feature_value = models.CharField(max_length=25, blank=False)


class ProductDescription(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=200, blank=False)


class Discount(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField()
    init_date = models.DateTimeField()
    duration = models.IntegerField()


class Comment(models.Model):
    subject = models.CharField(max_length=15, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    discount_amount = models.FloatField()


class Shipments(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField(auto_now_add=True)


class OrderList(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    number = models.IntegerField()


class QA(models.Model):
    subject = models.CharField(max_length=15, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

