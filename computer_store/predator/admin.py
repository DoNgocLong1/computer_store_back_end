from django.contrib import admin

from .models import Categories, Order, OrderItem, Product, ProductImages

# Register your models here.
admin.site.register(Categories)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ProductImages)
