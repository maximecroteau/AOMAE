from django.contrib import admin
from .models import Products
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'old_price', 'price', 'picture', 'stars')
    list_filter = ('name', 'old_price', 'price', 'stars')


admin.site.register(Products, ProductsAdmin)

# python manage.py migrate --run-syncdb