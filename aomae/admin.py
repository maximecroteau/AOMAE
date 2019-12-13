from django.contrib import admin
from .models import Products
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'picture', 'stars')
    list_filter = ('name', 'price', 'stars')


admin.site.register(Products, ProductsAdmin)
