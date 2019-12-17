from django.contrib import admin
from .models import Products
from .models import Color
from .models import Contact
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'picture', 'get_colors', 'gender', 'description', 'size_type', 'stars')
    list_filter = ('name', 'price', 'color', 'gender', 'description', 'stars')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color',)
    list_filter = ('color',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'name', 'mail', 'subject', 'message')
    list_filter = ('first_name', 'name', 'mail', 'subject', 'message')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Contact, ContactAdmin)
# python manage.py migrate --run-syncdb
