from django.contrib import admin
from .models import Product, Customer, ProductCategory, ProductDetails, ProductDescription

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(ProductDetails)
admin.site.register(ProductDescription)