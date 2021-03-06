from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'cover_image',  'product_name', 'price', 'available']

    @staticmethod
    def image(self, obj):
        from django.utils.html import format_html
        return format_html('<img width="50" src={} />', obj.cover_image.url)


admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(ProductDetails)
admin.site.register(Comment)
admin.site.register(Discount)
admin.site.register(ProductImage)