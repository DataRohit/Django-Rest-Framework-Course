# Import django admin
from django.contrib import admin

# Import all models
from products.models import *

from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "category")


# Register your models here.
admin.site.register(Product, ProductAdmin)
