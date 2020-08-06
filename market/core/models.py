from django.db import models
from django.contrib.auth.models import User


class Person(User):
    phone_number = models.CharField(max_length=13, blank=False)
    address = models.CharField(max_length=50, blank=False)
    national_ID = models.CharField(max_length=10, blank=False)


class Customer(Person):
    pass


class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=False)
    price = models.FloatField()
    available = models.BooleanField()
    inventory_count = models.IntegerField()
    description = models.TextField(blank=False)


class FavoriteList(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


class Category(models.Model):
    category_title = models.CharField(max_length=15, blank=False)


class ProductCategory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Seller(models.Model):
    deposit_amount = models.FloatField()
    rank = models.IntegerField()


class ProductSeller(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)


class ProductDetails(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=20, blank=False)
    feature_value = models.CharField(max_length=25, blank=False)


class Discount(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_code = models.CharField(blank=False, null=False)
    amount = models.FloatField()
    init_date = models.DateTimeField()
    duration = models.IntegerField()


class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=15, blank=False)
    content = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)


class CommentAdvantages(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    advantage = models.CharField(max_length=50, blank=False)


class CommentDisadvantages(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    disadvantage = models.CharField(max_length=50, blank=False)


class Orders(models.Model):
    order_status = (
        (1, "processing"),
        (2, "packing"),
        (3, "delivered"),
        (4, "received")
    )
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    seller_id = models.ForeignKey(Seller, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    discount_amount = models.FloatField()
    status = models.IntegerField(choices=order_status)


class Shipments(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField(auto_now_add=True)


class OrderList(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    number = models.IntegerField()
    discount = models.FloatField()


class Payments(models.Model):
    payment_status = (
        (1, "paid"),
        (2, "unpaid")
    )
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.IntegerField(choices=payment_status)
    payment_date = models.DateTimeField(auto_now_add=True)


class QA(models.Model):
    questinon = models.CharField(max_length=15, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)


class Ticket(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)


class TicketThread(models.Model):
    ticked_id = models.ForeignKey(QA, on_delete=models.CASCADE)
    answer_content = models.TextField()
    question_content = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)