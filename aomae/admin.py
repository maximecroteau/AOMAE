from django.contrib import admin
from .models import Products
from .models import Color
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'picture', 'get_colors', 'gender', 'description', 'size_type', 'stars')
    list_filter = ('name', 'price', 'color', 'gender', 'description', 'stars')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color',)
    list_filter = ('color',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Color, ColorAdmin)

# python manage.py migrate --run-syncdb
