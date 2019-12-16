from django.contrib import admin
from .models import Products
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'old_price', 'price', 'picture', 'gender', 'description', 'stars')
    list_filter = ('name', 'old_price', 'price', 'gender', 'description', 'stars')


admin.site.register(Products, ProductsAdmin)

# python manage.py migrate --run-syncdb