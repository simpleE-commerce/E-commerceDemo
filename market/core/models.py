from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=13, blank=False)
    address = models.CharField(max_length=50, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False)
    cover_image = models.ImageField(upload_to='product/cover_image', null=True, blank=False)
    price = models.FloatField()
    available = models.BooleanField()
    inventory_count = models.IntegerField()
    description = models.TextField(blank=False, default='')

    def __str__(self):
        return self.name


class Category(models.Model):
    category_title = models.CharField(max_length=15, blank=False)


class ProductCategory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class ProductFeatures(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=20, blank=False)
    feature_value = models.CharField(max_length=25, blank=False)


class Discount(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField()
    init_date = models.DateTimeField(default=timezone.now)
    until_date = models.DateTimeField(blank=False, default=timezone.now, null=True)
    # duration = models.IntegerField()


class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=15, blank=False)
    content = models.CharField(max_length=100, blank=False)
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
