from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "category")


# Register your models here.
admin.site.register(Product, ProductAdmin)
