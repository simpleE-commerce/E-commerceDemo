from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image',  'name', 'price', 'available']

    @staticmethod
    def image(self, obj):
        from django.utils.html import format_html
        return format_html('<img width="50" src={} />', obj.cover_image.url)


admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(ProductDetails)
admin.site.register(Comment)
admin.site.register(Discount)
