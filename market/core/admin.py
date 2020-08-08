from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(Comment)
admin.site.register(Discount)
admin.site.register(ProductFeatures)
